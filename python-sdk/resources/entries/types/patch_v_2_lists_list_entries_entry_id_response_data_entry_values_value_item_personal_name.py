# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic as pydantic

from ....core.datetime_utils import serialize_datetime
from .patch_v_2_lists_list_entries_entry_id_response_data_entry_values_value_item_personal_name_created_by_actor import (
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemPersonalNameCreatedByActor,
)


class PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemPersonalName(pydantic.BaseModel):
    active_from: dt.datetime = pydantic.Field(
        description='The point in time at which this value was made "active". `active_from` can be considered roughly analogous to `created_at`.'
    )
    active_until: typing.Optional[dt.datetime] = pydantic.Field(
        description="The point in time at which this value was deactivated. If `null`, the value is active."
    )
    created_by_actor: PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemPersonalNameCreatedByActor = (
        pydantic.Field(description="The actor that created this value.")
    )
    first_name: str = pydantic.Field(description="The first name.")
    last_name: str = pydantic.Field(description="The last name.")
    full_name: str = pydantic.Field(description="The full name.")

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
