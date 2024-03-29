# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .patch_v_2_lists_list_entries_entry_id_response_data_entry_values_value_item_actor_reference import (
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemActorReference,
)
from .patch_v_2_lists_list_entries_entry_id_response_data_entry_values_value_item_checkbox import (
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemCheckbox,
)
from .patch_v_2_lists_list_entries_entry_id_response_data_entry_values_value_item_currency import (
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemCurrency,
)
from .patch_v_2_lists_list_entries_entry_id_response_data_entry_values_value_item_date import (
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemDate,
)
from .patch_v_2_lists_list_entries_entry_id_response_data_entry_values_value_item_domain import (
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemDomain,
)
from .patch_v_2_lists_list_entries_entry_id_response_data_entry_values_value_item_email_address import (
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemEmailAddress,
)
from .patch_v_2_lists_list_entries_entry_id_response_data_entry_values_value_item_interaction import (
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemInteraction,
)
from .patch_v_2_lists_list_entries_entry_id_response_data_entry_values_value_item_location import (
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemLocation,
)
from .patch_v_2_lists_list_entries_entry_id_response_data_entry_values_value_item_number import (
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemNumber,
)
from .patch_v_2_lists_list_entries_entry_id_response_data_entry_values_value_item_personal_name import (
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemPersonalName,
)
from .patch_v_2_lists_list_entries_entry_id_response_data_entry_values_value_item_phone_number import (
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemPhoneNumber,
)
from .patch_v_2_lists_list_entries_entry_id_response_data_entry_values_value_item_rating import (
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemRating,
)
from .patch_v_2_lists_list_entries_entry_id_response_data_entry_values_value_item_record_reference import (
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemRecordReference,
)
from .patch_v_2_lists_list_entries_entry_id_response_data_entry_values_value_item_select import (
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemSelect,
)
from .patch_v_2_lists_list_entries_entry_id_response_data_entry_values_value_item_status import (
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemStatus,
)
from .patch_v_2_lists_list_entries_entry_id_response_data_entry_values_value_item_text import (
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemText,
)
from .patch_v_2_lists_list_entries_entry_id_response_data_entry_values_value_item_timestamp import (
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemTimestamp,
)


class PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItem_ActorReference(
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemActorReference
):
    attribute_type: typing_extensions.Literal["actor-reference"]

    class Config:
        frozen = True
        
        populate_by_name = True


class PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItem_Checkbox(
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemCheckbox
):
    attribute_type: typing_extensions.Literal["checkbox"]

    class Config:
        frozen = True
        
        populate_by_name = True


class PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItem_Currency(
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemCurrency
):
    attribute_type: typing_extensions.Literal["currency"]

    class Config:
        frozen = True
        
        populate_by_name = True


class PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItem_Date(
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemDate
):
    attribute_type: typing_extensions.Literal["date"]

    class Config:
        frozen = True
        
        populate_by_name = True


class PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItem_Domain(
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemDomain
):
    attribute_type: typing_extensions.Literal["domain"]

    class Config:
        frozen = True
        
        populate_by_name = True


class PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItem_EmailAddress(
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemEmailAddress
):
    attribute_type: typing_extensions.Literal["email-address"]

    class Config:
        frozen = True
        
        populate_by_name = True


class PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItem_RecordReference(
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemRecordReference
):
    attribute_type: typing_extensions.Literal["record-reference"]

    class Config:
        frozen = True
        
        populate_by_name = True


class PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItem_Interaction(
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemInteraction
):
    attribute_type: typing_extensions.Literal["interaction"]

    class Config:
        frozen = True
        
        populate_by_name = True


class PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItem_Location(
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemLocation
):
    attribute_type: typing_extensions.Literal["location"]

    class Config:
        frozen = True
        
        populate_by_name = True


class PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItem_Number(
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemNumber
):
    attribute_type: typing_extensions.Literal["number"]

    class Config:
        frozen = True
        
        populate_by_name = True


class PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItem_PersonalName(
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemPersonalName
):
    attribute_type: typing_extensions.Literal["personal-name"]

    class Config:
        frozen = True
        
        populate_by_name = True


class PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItem_PhoneNumber(
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemPhoneNumber
):
    attribute_type: typing_extensions.Literal["phone-number"]

    class Config:
        frozen = True
        
        populate_by_name = True


class PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItem_Status(
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemStatus
):
    attribute_type: typing_extensions.Literal["status"]

    class Config:
        frozen = True
        
        populate_by_name = True


class PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItem_Rating(
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemRating
):
    attribute_type: typing_extensions.Literal["rating"]

    class Config:
        frozen = True
        
        populate_by_name = True


class PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItem_Select(
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemSelect
):
    attribute_type: typing_extensions.Literal["select"]

    class Config:
        frozen = True
        
        populate_by_name = True


class PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItem_Text(
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemText
):
    attribute_type: typing_extensions.Literal["text"]

    class Config:
        frozen = True
        
        populate_by_name = True


class PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItem_Timestamp(
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemTimestamp
):
    attribute_type: typing_extensions.Literal["timestamp"]

    class Config:
        frozen = True
        
        populate_by_name = True


PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItem = typing.Union[
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItem_ActorReference,
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItem_Checkbox,
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItem_Currency,
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItem_Date,
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItem_Domain,
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItem_EmailAddress,
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItem_RecordReference,
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItem_Interaction,
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItem_Location,
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItem_Number,
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItem_PersonalName,
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItem_PhoneNumber,
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItem_Status,
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItem_Rating,
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItem_Select,
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItem_Text,
    PatchV2ListsListEntriesEntryIdResponseDataEntryValuesValueItem_Timestamp,
]
