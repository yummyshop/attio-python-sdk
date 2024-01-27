# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .get_v_2_lists_list_entries_entry_id_attributes_attribute_values_response_data_item_actor_reference import (
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemActorReference,
)
from .get_v_2_lists_list_entries_entry_id_attributes_attribute_values_response_data_item_checkbox import (
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemCheckbox,
)
from .get_v_2_lists_list_entries_entry_id_attributes_attribute_values_response_data_item_currency import (
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemCurrency,
)
from .get_v_2_lists_list_entries_entry_id_attributes_attribute_values_response_data_item_date import (
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemDate,
)
from .get_v_2_lists_list_entries_entry_id_attributes_attribute_values_response_data_item_domain import (
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemDomain,
)
from .get_v_2_lists_list_entries_entry_id_attributes_attribute_values_response_data_item_email_address import (
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemEmailAddress,
)
from .get_v_2_lists_list_entries_entry_id_attributes_attribute_values_response_data_item_interaction import (
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemInteraction,
)
from .get_v_2_lists_list_entries_entry_id_attributes_attribute_values_response_data_item_location import (
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemLocation,
)
from .get_v_2_lists_list_entries_entry_id_attributes_attribute_values_response_data_item_number import (
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemNumber,
)
from .get_v_2_lists_list_entries_entry_id_attributes_attribute_values_response_data_item_personal_name import (
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemPersonalName,
)
from .get_v_2_lists_list_entries_entry_id_attributes_attribute_values_response_data_item_phone_number import (
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemPhoneNumber,
)
from .get_v_2_lists_list_entries_entry_id_attributes_attribute_values_response_data_item_rating import (
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemRating,
)
from .get_v_2_lists_list_entries_entry_id_attributes_attribute_values_response_data_item_record_reference import (
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemRecordReference,
)
from .get_v_2_lists_list_entries_entry_id_attributes_attribute_values_response_data_item_select import (
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemSelect,
)
from .get_v_2_lists_list_entries_entry_id_attributes_attribute_values_response_data_item_status import (
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemStatus,
)
from .get_v_2_lists_list_entries_entry_id_attributes_attribute_values_response_data_item_text import (
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemText,
)
from .get_v_2_lists_list_entries_entry_id_attributes_attribute_values_response_data_item_timestamp import (
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemTimestamp,
)


class GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItem_ActorReference(
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemActorReference
):
    attribute_type: typing_extensions.Literal["actor-reference"]

    class Config:
        frozen = True
        
        allow_population_by_field_name = True


class GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItem_Checkbox(
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemCheckbox
):
    attribute_type: typing_extensions.Literal["checkbox"]

    class Config:
        frozen = True
        
        allow_population_by_field_name = True


class GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItem_Currency(
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemCurrency
):
    attribute_type: typing_extensions.Literal["currency"]

    class Config:
        frozen = True
        
        allow_population_by_field_name = True


class GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItem_Date(
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemDate
):
    attribute_type: typing_extensions.Literal["date"]

    class Config:
        frozen = True
        
        allow_population_by_field_name = True


class GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItem_Domain(
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemDomain
):
    attribute_type: typing_extensions.Literal["domain"]

    class Config:
        frozen = True
        
        allow_population_by_field_name = True


class GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItem_EmailAddress(
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemEmailAddress
):
    attribute_type: typing_extensions.Literal["email-address"]

    class Config:
        frozen = True
        
        allow_population_by_field_name = True


class GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItem_RecordReference(
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemRecordReference
):
    attribute_type: typing_extensions.Literal["record-reference"]

    class Config:
        frozen = True
        
        allow_population_by_field_name = True


class GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItem_Interaction(
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemInteraction
):
    attribute_type: typing_extensions.Literal["interaction"]

    class Config:
        frozen = True
        
        allow_population_by_field_name = True


class GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItem_Location(
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemLocation
):
    attribute_type: typing_extensions.Literal["location"]

    class Config:
        frozen = True
        
        allow_population_by_field_name = True


class GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItem_Number(
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemNumber
):
    attribute_type: typing_extensions.Literal["number"]

    class Config:
        frozen = True
        
        allow_population_by_field_name = True


class GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItem_PersonalName(
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemPersonalName
):
    attribute_type: typing_extensions.Literal["personal-name"]

    class Config:
        frozen = True
        
        allow_population_by_field_name = True


class GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItem_PhoneNumber(
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemPhoneNumber
):
    attribute_type: typing_extensions.Literal["phone-number"]

    class Config:
        frozen = True
        
        allow_population_by_field_name = True


class GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItem_Status(
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemStatus
):
    attribute_type: typing_extensions.Literal["status"]

    class Config:
        frozen = True
        
        allow_population_by_field_name = True


class GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItem_Rating(
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemRating
):
    attribute_type: typing_extensions.Literal["rating"]

    class Config:
        frozen = True
        
        allow_population_by_field_name = True


class GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItem_Select(
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemSelect
):
    attribute_type: typing_extensions.Literal["select"]

    class Config:
        frozen = True
        
        allow_population_by_field_name = True


class GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItem_Text(
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemText
):
    attribute_type: typing_extensions.Literal["text"]

    class Config:
        frozen = True
        
        allow_population_by_field_name = True


class GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItem_Timestamp(
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItemTimestamp
):
    attribute_type: typing_extensions.Literal["timestamp"]

    class Config:
        frozen = True
        
        allow_population_by_field_name = True


GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItem = typing.Union[
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItem_ActorReference,
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItem_Checkbox,
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItem_Currency,
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItem_Date,
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItem_Domain,
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItem_EmailAddress,
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItem_RecordReference,
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItem_Interaction,
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItem_Location,
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItem_Number,
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItem_PersonalName,
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItem_PhoneNumber,
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItem_Status,
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItem_Rating,
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItem_Select,
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItem_Text,
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponseDataItem_Timestamp,
]
