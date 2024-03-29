from typing import Optional
from pydantic import BaseModel as BaseModelSchema, validator
import datetime

class EntryCreateSchema(BaseModelSchema):
    title: str
    content: Optional[str] = None

    class Config:
        orm_mode = True

    @validator("title")
    def title_length(cls, value, **kwargs):
        if len(value) > 100:
            raise ValueError(f"{value} cannot exceed 100")
        return value


class EntryListSchema(EntryCreateSchema):
    id: int
    timestamp: Optional[datetime.datetime] = datetime.datetime.utcnow()
    updated: Optional[datetime.datetime] = datetime.datetime.utcnow()




"""
id
title
content
timestamp
updated
"""