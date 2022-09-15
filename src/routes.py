from fastapi import APIRouter

from src.account.routes import router as account_router

router = APIRouter()

router.include_router(account_router, prefix='/account')