# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic as pydantic

from ..core.datetime_utils import serialize_datetime


class TaskLinkedRecordsItem(pydantic.BaseModel):
    target_object_id: str = pydantic.Field(
        description="The ID of the parent object the task refers to. At present, only `people` and `companies` are supported."
    )
    target_record_id: str = pydantic.Field(description="The ID of the parent record the task refers to.")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        
        json_encoders = {dt.datetime: serialize_datetime}
