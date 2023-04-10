from pydantic import BaseModel
from typing import Any, Callable
from fastapi import Request, Response
from fastapi.routing import APIRoute
import gzip

__all__ = ['BoeAiInferenceRequest','GzipRoute']

class BoeAiInferenceRequest(BaseModel):
    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
        
    alg_code: str
    system: str = None
    userId: str = 'postman' 
    sessionId: str =  "postman"
    router: str=  ""
    user: str =  "poatman"
    args: dict  = {}  # img_base64 : 'base64 pic'
    
    

    
    
class GzipRequest(Request):
    async def body(self) -> bytes:
        if not hasattr(self, "_body"):
            body = await super().body()
            if "gzip" in self.headers.getlist("Content-Encoding"):
                body = gzip.decompress(body)
            self._body = body
        return self._body


class GzipRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            request = GzipRequest(request.scope, request.receive)
            return await original_route_handler(request)

        return custom_route_handler