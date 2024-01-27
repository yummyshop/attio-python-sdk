# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic.v1 as pydantic

from ..core.datetime_utils import serialize_datetime
from .comment import Comment
from .thread_id import ThreadId


class Thread(pydantic.BaseModel):
    id: ThreadId
    comments: typing.List[Comment] = pydantic.Field(
        description="An array of comments in the thread, sorted by `created_at`."
    )
    created_at: str = pydantic.Field(description="When the thread was created.")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
