from fastapi import APIRouter

from src.routes import router as src_router

router = APIRouter()

router.include_router(src_router, prefix='/api/v1')