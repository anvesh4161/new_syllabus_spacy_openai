from pydantic import BaseModel

class RequestSchema(BaseModel):
    request_id: str
    text: str