# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .post_v_2_lists_list_entries_query_response_data_item_entry_values_value_item_actor_reference import (
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemActorReference,
)
from .post_v_2_lists_list_entries_query_response_data_item_entry_values_value_item_checkbox import (
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemCheckbox,
)
from .post_v_2_lists_list_entries_query_response_data_item_entry_values_value_item_currency import (
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemCurrency,
)
from .post_v_2_lists_list_entries_query_response_data_item_entry_values_value_item_date import (
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemDate,
)
from .post_v_2_lists_list_entries_query_response_data_item_entry_values_value_item_domain import (
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemDomain,
)
from .post_v_2_lists_list_entries_query_response_data_item_entry_values_value_item_email_address import (
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemEmailAddress,
)
from .post_v_2_lists_list_entries_query_response_data_item_entry_values_value_item_interaction import (
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemInteraction,
)
from .post_v_2_lists_list_entries_query_response_data_item_entry_values_value_item_location import (
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemLocation,
)
from .post_v_2_lists_list_entries_query_response_data_item_entry_values_value_item_number import (
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemNumber,
)
from .post_v_2_lists_list_entries_query_response_data_item_entry_values_value_item_personal_name import (
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemPersonalName,
)
from .post_v_2_lists_list_entries_query_response_data_item_entry_values_value_item_phone_number import (
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemPhoneNumber,
)
from .post_v_2_lists_list_entries_query_response_data_item_entry_values_value_item_rating import (
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemRating,
)
from .post_v_2_lists_list_entries_query_response_data_item_entry_values_value_item_record_reference import (
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemRecordReference,
)
from .post_v_2_lists_list_entries_query_response_data_item_entry_values_value_item_select import (
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemSelect,
)
from .post_v_2_lists_list_entries_query_response_data_item_entry_values_value_item_status import (
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemStatus,
)
from .post_v_2_lists_list_entries_query_response_data_item_entry_values_value_item_text import (
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemText,
)
from .post_v_2_lists_list_entries_query_response_data_item_entry_values_value_item_timestamp import (
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemTimestamp,
)


class PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItem_ActorReference(
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemActorReference
):
    attribute_type: typing_extensions.Literal["actor-reference"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItem_Checkbox(
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemCheckbox
):
    attribute_type: typing_extensions.Literal["checkbox"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItem_Currency(
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemCurrency
):
    attribute_type: typing_extensions.Literal["currency"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItem_Date(
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemDate
):
    attribute_type: typing_extensions.Literal["date"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItem_Domain(
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemDomain
):
    attribute_type: typing_extensions.Literal["domain"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItem_EmailAddress(
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemEmailAddress
):
    attribute_type: typing_extensions.Literal["email-address"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItem_RecordReference(
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemRecordReference
):
    attribute_type: typing_extensions.Literal["record-reference"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItem_Interaction(
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemInteraction
):
    attribute_type: typing_extensions.Literal["interaction"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItem_Location(
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemLocation
):
    attribute_type: typing_extensions.Literal["location"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItem_Number(
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemNumber
):
    attribute_type: typing_extensions.Literal["number"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItem_PersonalName(
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemPersonalName
):
    attribute_type: typing_extensions.Literal["personal-name"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItem_PhoneNumber(
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemPhoneNumber
):
    attribute_type: typing_extensions.Literal["phone-number"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItem_Status(
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemStatus
):
    attribute_type: typing_extensions.Literal["status"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItem_Rating(
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemRating
):
    attribute_type: typing_extensions.Literal["rating"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItem_Select(
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemSelect
):
    attribute_type: typing_extensions.Literal["select"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItem_Text(
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemText
):
    attribute_type: typing_extensions.Literal["text"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItem_Timestamp(
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemTimestamp
):
    attribute_type: typing_extensions.Literal["timestamp"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItem = typing.Union[
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItem_ActorReference,
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItem_Checkbox,
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItem_Currency,
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItem_Date,
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItem_Domain,
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItem_EmailAddress,
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItem_RecordReference,
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItem_Interaction,
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItem_Location,
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItem_Number,
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItem_PersonalName,
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItem_PhoneNumber,
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItem_Status,
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItem_Rating,
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItem_Select,
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItem_Text,
    PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItem_Timestamp,
]