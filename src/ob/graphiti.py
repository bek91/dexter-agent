import os
from typing import Optional, List

import requests

from ob.schemas import SearchStrategy

API_KEY = os.getenv("GRAPHITI_API_KEY")
BASE_URL = "http://127.0.0.1:8000"


def _default_group_ids() -> Optional[List[str]]:
    env_val = os.getenv("GROUP_ID", "").strip()
    if not env_val:
        return None
    # Support comma-separated values
    return [g.strip() for g in env_val.split(",") if g.strip()]


DEFAULT_GROUP_IDS = _default_group_ids()


def search_advanced(
    query: str,
    center_node_uuid: Optional[str] = None,
    api_key: Optional[str] = API_KEY,
    base_url: str = BASE_URL,
    strategy: SearchStrategy = SearchStrategy.RRF,
):
    """
    Call the local Graphiti /search_advanced endpoint.

    Only `query` is required. Group IDs are always injected from the
    environment (GROUP_ID, comma-separated) and are not tool inputs.
    """
    url = f"{base_url}/search_advanced"
    headers = {
        "Content-Type": "application/json",
        "X-API-Key": api_key or "",
    }

    # Some backends expect the strategy under key 'recipe'.
    payload = {
        "query": query,
        "group_ids": DEFAULT_GROUP_IDS,
        "center_node_uuid": center_node_uuid,
        "recipe": strategy.value if isinstance(strategy, SearchStrategy) else str(strategy),
    }
    # Remove keys with None values for a clean payload
    payload = {k: v for k, v in payload.items() if v is not None}

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()
