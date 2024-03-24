from fastapi import APIRouter

from app.api.routers.ya_profi.ya_profi_router import router as ya_profi_router

router = APIRouter()

router.include_router(ya_profi_router)
