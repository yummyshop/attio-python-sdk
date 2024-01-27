# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic.v1 as pydantic

from ..core.datetime_utils import serialize_datetime
from .note_created_by_actor import NoteCreatedByActor
from .note_id import NoteId


class Note(pydantic.BaseModel):
    id: NoteId
    parent_object: str = pydantic.Field(description="The slug or ID of the parent object the note belongs to.")
    parent_record_id: str = pydantic.Field(description="The ID of the parent record the note belongs to.")
    title: str = pydantic.Field(description="The note title. The title is plaintext only and has no formatting.")
    content_plaintext: str = pydantic.Field(
        description="The plaintext representation of the note content. The line feed character `\n` represents new lines within the note content."
    )
    created_by_actor: NoteCreatedByActor = pydantic.Field(description="The actor that created this note.")
    created_at: str = pydantic.Field(description="When the note was created.")

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
