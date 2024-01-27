# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic as pydantic

from ..core.datetime_utils import serialize_datetime
from .comment_author import CommentAuthor
from .comment_entry import CommentEntry
from .comment_id import CommentId
from .comment_record import CommentRecord
from .comment_resolved_by import CommentResolvedBy


class Comment(pydantic.BaseModel):
    id: CommentId
    thread_id: str = pydantic.Field(description="The ID of the thread the comment belongs to.")
    content_plaintext: str = pydantic.Field(
        description="A plaintext representation of the content of the comment. References to workspace members are cast into email addresses, all other stylistic elements are removed."
    )
    entry: typing.Optional[CommentEntry] = pydantic.Field(
        description="The entry the comment belongs to, `null` for comments on records."
    )
    record: CommentRecord = pydantic.Field(description="The record the comment belongs to.")
    resolved_at: typing.Optional[str] = pydantic.Field(description="Whether the comment is resolved.")
    resolved_by: CommentResolvedBy = pydantic.Field(description="The actor that resolved this comment.")
    created_at: str = pydantic.Field(description="When the note was created.")
    author: CommentAuthor = pydantic.Field(
        description="Who wrote this comment. Note that the API provides the ability for API tokens to write comments on behalf of other actors."
    )

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
