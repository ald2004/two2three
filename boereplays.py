from pydantic import BaseModel
from typing import Any, Callable
from fastapi import Request, Response
from fastapi.routing import APIRoute
import gzip

__all__ = ['BoeAiInferenceReplay']


    
class BoeAiInferenceReplay(BaseModel):
    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
        
    retCode:str = 0
    retMsg:str = 'ok'
    args:dict = {}