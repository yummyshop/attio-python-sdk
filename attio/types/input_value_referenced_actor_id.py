# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic as pydantic
import typing_extensions

from ..core.datetime_utils import serialize_datetime


class InputValueReferencedActorId(pydantic.BaseModel):
    referenced_actor_type: typing_extensions.Literal["workspace-member"]
    referenced_actor_id: str = pydantic.Field(description="The ID of the referenced Actor.")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        
        json_encoders = {dt.datetime: serialize_datetime}
