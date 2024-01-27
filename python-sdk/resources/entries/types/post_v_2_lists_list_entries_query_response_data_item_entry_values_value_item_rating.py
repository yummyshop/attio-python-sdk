# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic.v1 as pydantic

from ....core.datetime_utils import serialize_datetime
from .post_v_2_lists_list_entries_query_response_data_item_entry_values_value_item_rating_created_by_actor import (
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemRatingCreatedByActor,
)


class PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemRating(pydantic.BaseModel):
    active_from: dt.datetime = pydantic.Field(
        description='The point in time at which this value was made "active". `active_from` can be considered roughly analogous to `created_at`.'
    )
    active_until: typing.Optional[dt.datetime] = pydantic.Field(
        description="The point in time at which this value was deactivated. If `null`, the value is active."
    )
    created_by_actor: PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemRatingCreatedByActor = (
        pydantic.Field(description="The actor that created this value.")
    )
    value: float = pydantic.Field(description="A number between 0 and 5 (inclusive) to represent a star rating.")

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