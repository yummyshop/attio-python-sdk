# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic as pydantic

from ....core.datetime_utils import serialize_datetime
from .post_v_2_lists_list_entries_query_request_sorts_item_attribute_direction import (
    PostV2ListsListEntriesQueryRequestSortsItemAttributeDirection,
)


class PostV2ListsListEntriesQueryRequestSortsItemAttribute(pydantic.BaseModel):
    """
    Sort by attribute
    """

    direction: PostV2ListsListEntriesQueryRequestSortsItemAttributeDirection = pydantic.Field(
        description="The direction to sort the results by."
    )
    attribute: str = pydantic.Field(description="A slug or ID to identify the attribute to sort by.")
    field: typing.Optional[str] = pydantic.Field(
        description='Which field on the value to sort by e.g. "last_name" on a name value.'
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
