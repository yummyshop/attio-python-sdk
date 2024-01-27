# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic.v1 as pydantic

from ....core.datetime_utils import serialize_datetime


class GetV2ObjectsObjectRecordsRecordIdResponseDataId(pydantic.BaseModel):
    workspace_id: str = pydantic.Field(description="A UUID identifying the workspace this record belongs to.")
    object_id: str = pydantic.Field(description="A UUID identifying the object this record belongs to.")
    record_id: str = pydantic.Field(description="A UUID identifying this record.")

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
