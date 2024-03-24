from enum import Enum

from fastapi import APIRouter
from pydantic.main import BaseModel

from app.service.host_manager.host_manager import get_free_host
from app.service.integration.host_creator.host_creator import create_host

router = APIRouter(
    tags=["Ya profi methods"],
)


class Response(BaseModel):
    class ResultEnum(Enum):
        OK = 'OK'
        NOT_OK = 'NOT_OK'

    result: ResultEnum
    host_id: int


class Request(BaseModel):
    id: int
    size: int
    task: str


@router.post(
    "/reserve_host",
    response_model=Response,
    description="Reserves host",
)
async def register_qr(
        request: Request,
):
    host = get_free_host(request.size)

    if host:
        create_host(request.task, request.size)

    return Request()
