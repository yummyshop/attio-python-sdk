# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic as pydantic

from ....core.datetime_utils import serialize_datetime
from .get_v_2_lists_list_entries_entry_id_attributes_attribute_values_response_data_item_number_created_by_actor import (
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemNumberCreatedByActor,
)


class GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemNumber(pydantic.BaseModel):
    active_from: dt.datetime = pydantic.Field(
        description='The point in time at which this value was made "active". `active_from` can be considered roughly analogous to `created_at`.'
    )
    active_until: typing.Optional[dt.datetime] = pydantic.Field(
        description="The point in time at which this value was deactivated. If `null`, the value is active."
    )
    created_by_actor: GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemNumberCreatedByActor = (
        pydantic.Field(description="The actor that created this value.")
    )
    value: float = pydantic.Field(description="Numbers are persisted as 64 bit floats.")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        
        json_encoders = {dt.datetime: serialize_datetime}
