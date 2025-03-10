from fastapi import  FastAPI

from contextlib import asynccontextmanager
from db import criate_tabels, delete_tabels

from router import router as tasks_router





@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    await delete_tabels()
    print("base clear")
    await criate_tabels()
    print("base create")
    yield
    # Clean up the ML models and release the resources
    print("end")
    

app=FastAPI(lifespan=lifespan)
app.include_router(tasks_router)


    
    
    
    

