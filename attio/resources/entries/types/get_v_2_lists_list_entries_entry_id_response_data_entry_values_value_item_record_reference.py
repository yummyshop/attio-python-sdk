# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic as pydantic

from ....core.datetime_utils import serialize_datetime
from .get_v_2_lists_list_entries_entry_id_response_data_entry_values_value_item_record_reference_created_by_actor import (
    GetV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemRecordReferenceCreatedByActor,
)


class GetV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemRecordReference(pydantic.BaseModel):
    active_from: dt.datetime = pydantic.Field(
        description='The point in time at which this value was made "active". `active_from` can be considered roughly analogous to `created_at`.'
    )
    active_until: typing.Optional[dt.datetime] = pydantic.Field(
        description="The point in time at which this value was deactivated. If `null`, the value is active."
    )
    created_by_actor: GetV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemRecordReferenceCreatedByActor = (
        pydantic.Field(description="The actor that created this value.")
    )
    target_object: str = pydantic.Field(
        description="A slug identifying the object that the referenced record belongs to."
    )
    target_record_id: str = pydantic.Field(description="A UUID to identify the referenced record.")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        
        json_encoders = {dt.datetime: serialize_datetime}
