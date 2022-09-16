from fastapi import APIRouter

from src.account.routes import router as account_router
from src.auth.routes import router as auth_router

router = APIRouter()

router.include_router(account_router, prefix='/account', tags=['users'])
router.include_router(auth_router, prefix='/auth', tags=['auth'])
