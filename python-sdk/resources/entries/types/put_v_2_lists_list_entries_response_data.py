# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic.v1 as pydantic

from ....core.datetime_utils import serialize_datetime
from .put_v_2_lists_list_entries_response_data_entry_values_value_item import (
    PutV2ListsListEntriesResponseDataEntryValuesValueItem,
)
from .put_v_2_lists_list_entries_response_data_id import PutV2ListsListEntriesResponseDataId


class PutV2ListsListEntriesResponseData(pydantic.BaseModel):
    id: PutV2ListsListEntriesResponseDataId
    parent_record_id: str = pydantic.Field(
        description="A UUID identifying the record that is parent of the list entry."
    )
    parent_object: str = pydantic.Field(
        description="A UUID or slug identifying the object that the parent record belongs to."
    )
    created_at: str = pydantic.Field(description="When this entry was created.")
    entry_values: typing.Dict[str, typing.List[PutV2ListsListEntriesResponseDataEntryValuesValueItem]] = pydantic.Field(
        description="A list of attribute values for the list entry (not attribute values for its parent record)."
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