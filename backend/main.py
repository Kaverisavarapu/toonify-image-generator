from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from backend.api.auth import router as auth_router
from backend.api.image import router as image_router
from backend.api.history import (
    router as history_router
)
from backend.api.admin import (
    router as admin_router
)
app = FastAPI(
    title="Toonify API"
)
from backend.api.profile import (
    router as profile_router
)
from backend.api.payment import (
    router as payment_router
)
# Routers
app.include_router(auth_router)
app.include_router(image_router)
app.include_router(history_router)
app.include_router(admin_router)
app.include_router(profile_router)
app.include_router(
    payment_router
)
# Serve uploaded images
from pathlib import Path

print("CURRENT DIR:", Path.cwd())
print("UPLOADS EXISTS:", Path("backend/uploads").exists())
print("ORIGINALS EXISTS:", Path("backend/uploads/originals").exists())
print("CARTOONS EXISTS:", Path("backend/uploads/cartoons").exists())
app.mount(
    "/uploads",
    StaticFiles(directory="backend/uploads"),
    name="uploads"
)


@app.get("/")
def home():
    return {
        "message": "Toonify Backend Running"
    }