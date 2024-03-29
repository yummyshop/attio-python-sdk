# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic as pydantic

from ....core.datetime_utils import serialize_datetime


class PostV2ListsListEntriesRequestData(pydantic.BaseModel):
    parent_record_id: str = pydantic.Field(
        description="A UUID identifying the record you want to add to the list. The record will become the 'parent' of the created list entry."
    )
    parent_object: str = pydantic.Field(
        description="A UUID or slug identifying the object that the added parent record belongs to."
    )
    entry_values: typing.Dict[str, typing.List[typing.Any]] = pydantic.Field(
        description="An object with an attribute `api_slug` or `attribute_id` as the key, and a single value (for single-select attributes), or an array of values (for single or multi-select attributes) as the values. For complete documentation on values for all attribute types, please see our [attribute type docs](/docs/attribute-types)."
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
