from typing import Annotated

from fastapi import Header, HTTPException


async def get_token_header(x_token: Annotated[str, Header()]):
    # print(x_token)
    # print('11111111111111111111')
    if x_token != "BoeAiInferenceRequest":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str):
    if token != "BoeAiInferenceRequest":
        raise HTTPException(status_code=400, detail="No token provided")
