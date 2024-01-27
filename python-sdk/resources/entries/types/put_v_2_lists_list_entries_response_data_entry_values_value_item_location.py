# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic as pydantic

from ....core.datetime_utils import serialize_datetime
from .put_v_2_lists_list_entries_response_data_entry_values_value_item_location_country_code import (
    PutV2ListsListEntriesResponseDataEntryValuesValueItemLocationCountryCode,
)
from .put_v_2_lists_list_entries_response_data_entry_values_value_item_location_created_by_actor import (
    PutV2ListsListEntriesResponseDataEntryValuesValueItemLocationCreatedByActor,
)


class PutV2ListsListEntriesResponseDataEntryValuesValueItemLocation(pydantic.BaseModel):
    active_from: dt.datetime = pydantic.Field(
        description='The point in time at which this value was made "active". `active_from` can be considered roughly analogous to `created_at`.'
    )
    active_until: typing.Optional[dt.datetime] = pydantic.Field(
        description="The point in time at which this value was deactivated. If `null`, the value is active."
    )
    created_by_actor: PutV2ListsListEntriesResponseDataEntryValuesValueItemLocationCreatedByActor = pydantic.Field(
        description="The actor that created this value."
    )
    line_1: typing.Optional[str] = pydantic.Field(
        description="The first line of the address. Note that this value is not currently represented in the UI but will be persisted and readable through API calls."
    )
    line_2: typing.Optional[str] = pydantic.Field(
        description="The second line of the address. Note that this value is not currently represented in the UI but will be persisted and readable through API calls."
    )
    line_3: typing.Optional[str] = pydantic.Field(
        description="The third line of the address. Note that this value is not currently represented in the UI but will be persisted and readable through API calls."
    )
    line_4: typing.Optional[str] = pydantic.Field(
        description="The fourth line of the address. Note that this value is not currently represented in the UI but will be persisted and readable through API calls."
    )
    locality: typing.Optional[str] = pydantic.Field(description="The town, neighborhood or area the location is in.")
    region: typing.Optional[str] = pydantic.Field(
        description="The state, county, province or region that the location is in."
    )
    postcode: typing.Optional[str] = pydantic.Field(
        description="The postcode or zip code for the location. Note that this value is not currently represented in the UI but will be persisted and readable through API calls.}"
    )
    country_code: typing.Optional[
        PutV2ListsListEntriesResponseDataEntryValuesValueItemLocationCountryCode
    ] = pydantic.Field(description="The ISO 3166-1 alpha-2 country code for the country this location is in.")
    latitude: typing.Optional[str] = pydantic.Field(
        description=(
            "The latitude of the location. Validated by the regular expression `/^[-+]?([1-8]?\d(\.\d+)?\n"
            "90(\.0+)?)$/`. Note that this value is not currently represented in the UI but will be persisted and readable through API calls.}\n"
        )
    )
    longitude: typing.Optional[str] = pydantic.Field(
        description=(
            "The longitude of the location. Validated by the regular expression `/^[-+]?(180(\.0+)?\n"
            "((1[0-7]\d)\n"
            "([1-9]?\d))(\.\d+)?)$/`\n"
        )
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
