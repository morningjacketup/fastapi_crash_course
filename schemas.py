from typing import Optional

from pydantic import BaseModel, ConfigDict


class STasksAdd(BaseModel):
    name: str
    description: str | None = None

class STask(STasksAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)

class STaskId(BaseModel):
    ok: bool = True
    task_id: int