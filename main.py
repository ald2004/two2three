from fastapi import Depends, FastAPI
from boerequests import *
from boereplays import *
from dependencies import get_token_header
# from internal import admin
# from routers import items, users
from logger import setup_logger


logger = setup_logger(name='two2three',output='./two2three.log')
app = FastAPI(dependencies=[Depends(get_token_header)])

# app = FastAPI()
app.router.route_class = GzipRoute

# app.include_router(users.router)
# app.include_router(items.router)
# app.include_router(
#     admin.router,
#     prefix="/admin",
#     tags=["admin"],
#     dependencies=[Depends(get_token_header)],
#     responses={418: {"description": "I'm a teapot"}},
# )
br = BoeAiInferenceReplay()

@app.post("/")
async def root(brq:BoeAiInferenceRequest):
    logger.debug('111111111111111111111111111111')
    # logger.debug(br)
    return br
