from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum
class Task(BaseModel):
    """Represents a single task in a task list."""
    id: int = Field(..., description="Unique identifier for the task.")
    description: str = Field(..., description="The description of the task.")
    done: bool = Field(False, description="Whether the task is completed.")

class TaskList(BaseModel):
    """Represents a list of tasks."""
    tasks: List[Task] = Field(..., description="The list of tasks.")

class IsDone(BaseModel):
    """Represents the boolean status of a task."""
    done: bool = Field(..., description="Whether the task is done or not.")

class Answer(BaseModel):
    """Represents an answer to the user's query."""
    answer: str = Field(..., description="A comprehensive answer to the user's query, including relevant numbers, data, reasoning, and insights.")


class SearchStrategy(str, Enum):
    RRF = 'RRF'
    MMR = 'MMR'
    CROSS_ENCODER = 'CROSS_ENCODER'

class AdvancedSearchInSchema(BaseModel):
    query: str = Field(..., description="The query to search for.")
    center_node_uuid: Optional[str] = Field(None, description="Optional center node UUID to anchor the search.")
    strategy: SearchStrategy = Field(SearchStrategy.RRF, description="Search strategy. Defaults to RRF.")


class SearchNodesInSchema(BaseModel):
    query: str = Field(..., description="The query to search for.")
    group_ids: Optional[List[str]] = Field(None, description="The group ids to search in.")
    center_node_uuid: Optional[str] = Field(None, description="The uuid of the center node to search from.")
    limit: Optional[int] = Field(None, description="Limit on the number of results to return.")
