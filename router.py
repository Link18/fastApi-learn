from typing import Annotated

from fastapi import Depends
from repository import TaskRepository
from schemas import STasksID, STasksAdd

from fastapi import APIRouter

router = APIRouter(
    prefix="/tasks",
    tags=["таски"]
)

@router.post("")
async def add_tasks(
    task: Annotated[STasksAdd,Depends()]
    )-> STasksID:
    task_id = await TaskRepository.add_one(task)
    return{
        "ok":True,
        "task_id" : task_id
           }

@router.get("")
async def get_tasks():
    tasks = await TaskRepository.find_all()
    return {"tasks":tasks}