# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic.v1 as pydantic

from ....core.datetime_utils import serialize_datetime
from .put_v_2_lists_list_entries_entry_id_response_data_entry_values_value_item_record_reference_created_by_actor_type import (
    PutV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemRecordReferenceCreatedByActorType,
)


class PutV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemRecordReferenceCreatedByActor(pydantic.BaseModel):
    """
    The actor that created this value.
    """

    id: typing.Optional[str] = pydantic.Field(description="An ID to identify the actor.")
    type: typing.Optional[
        PutV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemRecordReferenceCreatedByActorType
    ] = pydantic.Field(description="The type of actor. [Read more information on actor types here](/docs/actors).")

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
