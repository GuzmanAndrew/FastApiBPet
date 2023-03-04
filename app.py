from fastapi import FastAPI
from logic.v1.routes.user import user as user
from logic.v1.config.openapi import tags_metadata as tags_metadata
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Users API",
    description="a REST API using python and mysql",
    version="0.0.1",
    openapi_tags=tags_metadata,
)

origins = [
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user)
