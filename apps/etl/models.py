from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Message(BaseModel):
    created: datetime
    id: str
    int_id: str
    str_: str


class Log(BaseModel):
    created: datetime
    int_id: str
    str_: Optional[str]
    address: Optional[str]
