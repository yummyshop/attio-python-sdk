# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .post_v_2_lists_list_entries_response_data_entry_values_value_item_actor_reference import (
    PostV2ListsListEntriesResponseDataEntryValuesValueItemActorReference,
)
from .post_v_2_lists_list_entries_response_data_entry_values_value_item_checkbox import (
    PostV2ListsListEntriesResponseDataEntryValuesValueItemCheckbox,
)
from .post_v_2_lists_list_entries_response_data_entry_values_value_item_currency import (
    PostV2ListsListEntriesResponseDataEntryValuesValueItemCurrency,
)
from .post_v_2_lists_list_entries_response_data_entry_values_value_item_date import (
    PostV2ListsListEntriesResponseDataEntryValuesValueItemDate,
)
from .post_v_2_lists_list_entries_response_data_entry_values_value_item_domain import (
    PostV2ListsListEntriesResponseDataEntryValuesValueItemDomain,
)
from .post_v_2_lists_list_entries_response_data_entry_values_value_item_email_address import (
    PostV2ListsListEntriesResponseDataEntryValuesValueItemEmailAddress,
)
from .post_v_2_lists_list_entries_response_data_entry_values_value_item_interaction import (
    PostV2ListsListEntriesResponseDataEntryValuesValueItemInteraction,
)
from .post_v_2_lists_list_entries_response_data_entry_values_value_item_location import (
    PostV2ListsListEntriesResponseDataEntryValuesValueItemLocation,
)
from .post_v_2_lists_list_entries_response_data_entry_values_value_item_number import (
    PostV2ListsListEntriesResponseDataEntryValuesValueItemNumber,
)
from .post_v_2_lists_list_entries_response_data_entry_values_value_item_personal_name import (
    PostV2ListsListEntriesResponseDataEntryValuesValueItemPersonalName,
)
from .post_v_2_lists_list_entries_response_data_entry_values_value_item_phone_number import (
    PostV2ListsListEntriesResponseDataEntryValuesValueItemPhoneNumber,
)
from .post_v_2_lists_list_entries_response_data_entry_values_value_item_rating import (
    PostV2ListsListEntriesResponseDataEntryValuesValueItemRating,
)
from .post_v_2_lists_list_entries_response_data_entry_values_value_item_record_reference import (
    PostV2ListsListEntriesResponseDataEntryValuesValueItemRecordReference,
)
from .post_v_2_lists_list_entries_response_data_entry_values_value_item_select import (
    PostV2ListsListEntriesResponseDataEntryValuesValueItemSelect,
)
from .post_v_2_lists_list_entries_response_data_entry_values_value_item_status import (
    PostV2ListsListEntriesResponseDataEntryValuesValueItemStatus,
)
from .post_v_2_lists_list_entries_response_data_entry_values_value_item_text import (
    PostV2ListsListEntriesResponseDataEntryValuesValueItemText,
)
from .post_v_2_lists_list_entries_response_data_entry_values_value_item_timestamp import (
    PostV2ListsListEntriesResponseDataEntryValuesValueItemTimestamp,
)


class PostV2ListsListEntriesResponseDataEntryValuesValueItem_ActorReference(
    PostV2ListsListEntriesResponseDataEntryValuesValueItemActorReference
):
    attribute_type: typing_extensions.Literal["actor-reference"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ListsListEntriesResponseDataEntryValuesValueItem_Checkbox(
    PostV2ListsListEntriesResponseDataEntryValuesValueItemCheckbox
):
    attribute_type: typing_extensions.Literal["checkbox"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ListsListEntriesResponseDataEntryValuesValueItem_Currency(
    PostV2ListsListEntriesResponseDataEntryValuesValueItemCurrency
):
    attribute_type: typing_extensions.Literal["currency"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ListsListEntriesResponseDataEntryValuesValueItem_Date(
    PostV2ListsListEntriesResponseDataEntryValuesValueItemDate
):
    attribute_type: typing_extensions.Literal["date"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ListsListEntriesResponseDataEntryValuesValueItem_Domain(
    PostV2ListsListEntriesResponseDataEntryValuesValueItemDomain
):
    attribute_type: typing_extensions.Literal["domain"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ListsListEntriesResponseDataEntryValuesValueItem_EmailAddress(
    PostV2ListsListEntriesResponseDataEntryValuesValueItemEmailAddress
):
    attribute_type: typing_extensions.Literal["email-address"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ListsListEntriesResponseDataEntryValuesValueItem_RecordReference(
    PostV2ListsListEntriesResponseDataEntryValuesValueItemRecordReference
):
    attribute_type: typing_extensions.Literal["record-reference"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ListsListEntriesResponseDataEntryValuesValueItem_Interaction(
    PostV2ListsListEntriesResponseDataEntryValuesValueItemInteraction
):
    attribute_type: typing_extensions.Literal["interaction"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ListsListEntriesResponseDataEntryValuesValueItem_Location(
    PostV2ListsListEntriesResponseDataEntryValuesValueItemLocation
):
    attribute_type: typing_extensions.Literal["location"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ListsListEntriesResponseDataEntryValuesValueItem_Number(
    PostV2ListsListEntriesResponseDataEntryValuesValueItemNumber
):
    attribute_type: typing_extensions.Literal["number"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ListsListEntriesResponseDataEntryValuesValueItem_PersonalName(
    PostV2ListsListEntriesResponseDataEntryValuesValueItemPersonalName
):
    attribute_type: typing_extensions.Literal["personal-name"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ListsListEntriesResponseDataEntryValuesValueItem_PhoneNumber(
    PostV2ListsListEntriesResponseDataEntryValuesValueItemPhoneNumber
):
    attribute_type: typing_extensions.Literal["phone-number"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ListsListEntriesResponseDataEntryValuesValueItem_Status(
    PostV2ListsListEntriesResponseDataEntryValuesValueItemStatus
):
    attribute_type: typing_extensions.Literal["status"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ListsListEntriesResponseDataEntryValuesValueItem_Rating(
    PostV2ListsListEntriesResponseDataEntryValuesValueItemRating
):
    attribute_type: typing_extensions.Literal["rating"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ListsListEntriesResponseDataEntryValuesValueItem_Select(
    PostV2ListsListEntriesResponseDataEntryValuesValueItemSelect
):
    attribute_type: typing_extensions.Literal["select"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ListsListEntriesResponseDataEntryValuesValueItem_Text(
    PostV2ListsListEntriesResponseDataEntryValuesValueItemText
):
    attribute_type: typing_extensions.Literal["text"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ListsListEntriesResponseDataEntryValuesValueItem_Timestamp(
    PostV2ListsListEntriesResponseDataEntryValuesValueItemTimestamp
):
    attribute_type: typing_extensions.Literal["timestamp"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


PostV2ListsListEntriesResponseDataEntryValuesValueItem = typing.Union[
    PostV2ListsListEntriesResponseDataEntryValuesValueItem_ActorReference,
    PostV2ListsListEntriesResponseDataEntryValuesValueItem_Checkbox,
    PostV2ListsListEntriesResponseDataEntryValuesValueItem_Currency,
    PostV2ListsListEntriesResponseDataEntryValuesValueItem_Date,
    PostV2ListsListEntriesResponseDataEntryValuesValueItem_Domain,
    PostV2ListsListEntriesResponseDataEntryValuesValueItem_EmailAddress,
    PostV2ListsListEntriesResponseDataEntryValuesValueItem_RecordReference,
    PostV2ListsListEntriesResponseDataEntryValuesValueItem_Interaction,
    PostV2ListsListEntriesResponseDataEntryValuesValueItem_Location,
    PostV2ListsListEntriesResponseDataEntryValuesValueItem_Number,
    PostV2ListsListEntriesResponseDataEntryValuesValueItem_PersonalName,
    PostV2ListsListEntriesResponseDataEntryValuesValueItem_PhoneNumber,
    PostV2ListsListEntriesResponseDataEntryValuesValueItem_Status,
    PostV2ListsListEntriesResponseDataEntryValuesValueItem_Rating,
    PostV2ListsListEntriesResponseDataEntryValuesValueItem_Select,
    PostV2ListsListEntriesResponseDataEntryValuesValueItem_Text,
    PostV2ListsListEntriesResponseDataEntryValuesValueItem_Timestamp,
]