from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette import status
from src.app_config import app_settings
from src.app_config.config_redis import RedisRepository
from src.app_config.dependies import get_redis_repo
from src.database.database import database_accessor
from .app.api.router import router as api_router
from fastapi.middleware.cors import CORSMiddleware


def bind_exceptions(app: FastAPI) -> None:
    @app.exception_handler(Exception)
    async def unhandled_error(_: Request, exc: Exception) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": str(exc)},
        )


def bind_events(app: FastAPI) -> None:
    @app.on_event("startup")
    async def set_engine():
        db = database_accessor
        await db.run()
        app.state.db = db
        get_redis_repo.redis_repo = await RedisRepository.connect()

    @app.on_event("shutdown")
    async def close_engine():
        await app.state.db.stop()


def get_app() -> FastAPI:
    app = FastAPI(
        title="POMOSCH",
        version="0.1.0",
        description="POMOSCH api",
        docs_url="/docs",
        openapi_url="/api/test",
    )

    bind_events(app)
    bind_exceptions(app)
    app.include_router(api_router)
    app.add_middleware(
        CORSMiddleware,
        allow_origins="*",
        allow_credentials=True,
        allow_methods="*",
        allow_headers="*",
    )
    app.state.settings = app_settings
    return app


app = get_app()
