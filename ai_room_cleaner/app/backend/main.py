from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .services import ai_service, camera_service

app = FastAPI()

@app.post("/api/tasks")
async def create_task():
    return {"message": "Task created successfully"}

@app.get("/api/tasks")
async def get_tasks():
    return []

@app.put("/api/tasks/{task_id}")
async def update_task(task_id: int):
    return {"message": f"Task {task_id} updated successfully"}

@app.post("/api/analyze")
async def analyze_room():
    image_path = camera_service.get_image_path()
    messes = ai_service.get_ai_response(image_path)
    return {"messes": messes}

app.mount("/", StaticFiles(directory="/app/frontend", html=True), name="static")