from pydantic import BaseModel


class STasksAdd(BaseModel):
    name: str
    description: str|None
    
class STasks (STasksAdd):
    id:int

class STasksID (BaseModel):
    ok: bool=True
    task_id: int