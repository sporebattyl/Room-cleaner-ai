import asyncio
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
import bashio

from .services import ai_service, camera_service

# Load configuration
# cfg = config.get_settings()

app = FastAPI(
    title="AI Room Cleaner",
    description="A Home Assistant addon to keep your room clean with AI.",
    version="0.1.0"
)

@app.on_event("startup")
async def startup_event():
    """
    Event handler for application startup.
    This is where we will initialize the main background task.
    """
    bashio.log.info("AI Room Cleaner backend is starting up...")
    asyncio.create_task(main_loop())

@app.get("/api/health")
async def health_check():
    """
    A simple health check endpoint to confirm the API is running.
    """
    return {"status": "ok"}


@app.post("/api/tasks")
async def create_task():
    return {"message": "Task created successfully (placeholder)"}


@app.get("/api/tasks")
async def get_tasks():
    return []


@app.put("/api/tasks/{task_id}")
async def update_task(task_id: int):
    return {"message": f"Task {task_id} updated successfully (placeholder)"}


@app.post("/api/analyze")
async def analyze_room():
    """
    Triggers a room analysis.
    """
    bashio.log.info("API: Received request to analyze room.")
    image_path = camera_service.get_placeholder_image()
    messes = ai_service.analyze_image_with_ai(image_path)
    return {"messes_identified": messes}


# Placeholder for the main analysis loop
async def main_loop():
    """
    The main background task that periodically fetches the camera feed,
    analyzes it, and updates the to-do list.
    """
    bashio.log.info("Starting main analysis loop...")
    update_frequency = bashio.config.get('update_frequency', 60)

    while True:
        bashio.log.info("Running cleanliness analysis...")
        image_path = camera_service.get_placeholder_image()
        ai_service.analyze_image_with_ai(image_path)
        await asyncio.sleep(update_frequency)

# Mount the frontend
app.mount("/", StaticFiles(directory="app/frontend", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)