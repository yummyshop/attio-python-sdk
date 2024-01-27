# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic as pydantic

from ..core.datetime_utils import serialize_datetime
from .select_option_id import SelectOptionId


class SelectOption(pydantic.BaseModel):
    id: SelectOptionId
    title: str = pydantic.Field(description="The title of the select option")
    is_archived: bool = pydantic.Field(
        description="Whether or not to archive the select option. See our [archiving guide](/docs/archiving-vs-deleting) for more information on archiving."
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        
        json_encoders = {dt.datetime: serialize_datetime}
