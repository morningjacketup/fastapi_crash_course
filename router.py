from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import STask, STaskId, STasksAdd

router = APIRouter(prefix="/tasks", tags=["Таски"])

@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.get_tasks()
    return tasks

@router.post("")
async def add_task(
    task: STasksAdd = Depends()
) -> STaskId:
    new_task_id = await TaskRepository.add_task(task)
    return {"task_id": new_task_id}