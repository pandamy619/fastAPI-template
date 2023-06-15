from fastapi import FastAPI

from fastapi_template.auth.router import router as auth_router


def routers(app: FastAPI) -> None:
    app.include_router(router=auth_router)

