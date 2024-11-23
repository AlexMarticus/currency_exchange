from fastapi import APIRouter


currency_router = APIRouter(
    prefix="/currency",
    tags=["Currency"]
)


@currency_router.get("/exchange")
async def get_exchange():
    pass


@currency_router.get("/list")
async def get_list():
    pass
