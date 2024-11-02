from fastapi import APIRouter


auth_router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@auth_router.post("/login")
async def get_todos():
    pass


@auth_router.post("/register")
async def create_todo():
    pass
