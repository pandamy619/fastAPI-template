from typing import Any

from fastapi import FastAPI
from fastapi_template.routers import routers
from starlette.middleware.cors import CORSMiddleware

__version__ = "0.1.0"


def create_app() -> Any:
    app = FastAPI(docs_url="/api/docs", openapi_url="/api/openapi.json")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    routers(app=app)
    return app
