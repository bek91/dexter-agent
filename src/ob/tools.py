from langchain.tools import tool
from typing import List, Callable, Optional

from ob.schemas import AdvancedSearchInSchema, SearchStrategy
from ob import graphiti

####################################
# SearchTools
####################################

@tool(args_schema=AdvancedSearchInSchema)
def advanced_search(
    query: str,
    center_node_uuid: Optional[str] = None,
    strategy: SearchStrategy = SearchStrategy.RRF,
) -> dict:
    """Primary search tool for the Thesis knowledge graph. Returns nodes, edges, communities, and metadata.
    Inputs: query (required), optional center_node_uuid, optional strategy (defaults RRF).
    Group IDs are injected from environment (GROUP_ID) and not part of the tool inputs.
    """
    return graphiti.search_advanced(
        query=query,
        center_node_uuid=center_node_uuid,
        strategy=strategy,
    )


TOOLS: List[Callable[..., any]] = [advanced_search]

RISKY_TOOLS = {}  # guardrail: require confirmation
