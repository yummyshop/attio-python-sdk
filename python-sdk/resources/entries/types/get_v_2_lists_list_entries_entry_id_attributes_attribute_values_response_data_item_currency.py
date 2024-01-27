# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic.v1 as pydantic

from ....core.datetime_utils import serialize_datetime
from .get_v_2_lists_list_entries_entry_id_attributes_attribute_values_response_data_item_currency_created_by_actor import (
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemCurrencyCreatedByActor,
)
from .get_v_2_lists_list_entries_entry_id_attributes_attribute_values_response_data_item_currency_currency_code import (
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemCurrencyCurrencyCode,
)


class GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemCurrency(pydantic.BaseModel):
    active_from: dt.datetime = pydantic.Field(
        description='The point in time at which this value was made "active". `active_from` can be considered roughly analogous to `created_at`.'
    )
    active_until: typing.Optional[dt.datetime] = pydantic.Field(
        description="The point in time at which this value was deactivated. If `null`, the value is active."
    )
    created_by_actor: GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemCurrencyCreatedByActor = (
        pydantic.Field(description="The actor that created this value.")
    )
    currency_value: float = pydantic.Field(
        description="A numerical representation of the currency value. A decimal with a max of 4 decimal places."
    )
    currency_code: typing.Optional[
        GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemCurrencyCurrencyCode
    ] = pydantic.Field(description="The ISO4217 currency code representing the currency that the value is stored in.")

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
