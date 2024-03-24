import logging

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import router
from app.settings import settings


def service_log():
    logging.basicConfig(level=logging.ERROR)
    logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


# app = FastAPI()
app = FastAPI(
    title=settings.SERVICE_NAME,
    root_path=settings.ROOT_PATH,
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

if __name__ == "__main__":
    service_log()
    uvicorn.run("main:app", host=settings.API_host, port=settings.API_port, backlog=4096)
