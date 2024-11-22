from fastapi import APIRouter


auth_router = APIRouter(
    prefix="/currency",
    tags=["Currency"]
)


@auth_router.get("/exchange")
async def get_exchange():
    pass


@auth_router.get("/list")
async def get_list():
    pass
