# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .post_v_2_objects_object_records_query_response_data_item_values_value_item_actor_reference import (
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemActorReference,
)
from .post_v_2_objects_object_records_query_response_data_item_values_value_item_checkbox import (
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemCheckbox,
)
from .post_v_2_objects_object_records_query_response_data_item_values_value_item_currency import (
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemCurrency,
)
from .post_v_2_objects_object_records_query_response_data_item_values_value_item_date import (
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemDate,
)
from .post_v_2_objects_object_records_query_response_data_item_values_value_item_domain import (
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemDomain,
)
from .post_v_2_objects_object_records_query_response_data_item_values_value_item_email_address import (
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemEmailAddress,
)
from .post_v_2_objects_object_records_query_response_data_item_values_value_item_interaction import (
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemInteraction,
)
from .post_v_2_objects_object_records_query_response_data_item_values_value_item_location import (
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemLocation,
)
from .post_v_2_objects_object_records_query_response_data_item_values_value_item_number import (
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemNumber,
)
from .post_v_2_objects_object_records_query_response_data_item_values_value_item_personal_name import (
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemPersonalName,
)
from .post_v_2_objects_object_records_query_response_data_item_values_value_item_phone_number import (
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemPhoneNumber,
)
from .post_v_2_objects_object_records_query_response_data_item_values_value_item_rating import (
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemRating,
)
from .post_v_2_objects_object_records_query_response_data_item_values_value_item_record_reference import (
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemRecordReference,
)
from .post_v_2_objects_object_records_query_response_data_item_values_value_item_select import (
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemSelect,
)
from .post_v_2_objects_object_records_query_response_data_item_values_value_item_status import (
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemStatus,
)
from .post_v_2_objects_object_records_query_response_data_item_values_value_item_text import (
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemText,
)
from .post_v_2_objects_object_records_query_response_data_item_values_value_item_timestamp import (
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemTimestamp,
)


class PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItem_ActorReference(
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemActorReference
):
    attribute_type: typing_extensions.Literal["actor-reference"]

    class Config:
        frozen = True
        
        populate_by_name = True


class PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItem_Checkbox(
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemCheckbox
):
    attribute_type: typing_extensions.Literal["checkbox"]

    class Config:
        frozen = True
        
        populate_by_name = True


class PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItem_Currency(
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemCurrency
):
    attribute_type: typing_extensions.Literal["currency"]

    class Config:
        frozen = True
        
        populate_by_name = True


class PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItem_Date(
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemDate
):
    attribute_type: typing_extensions.Literal["date"]

    class Config:
        frozen = True
        
        populate_by_name = True


class PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItem_Domain(
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemDomain
):
    attribute_type: typing_extensions.Literal["domain"]

    class Config:
        frozen = True
        
        populate_by_name = True


class PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItem_EmailAddress(
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemEmailAddress
):
    attribute_type: typing_extensions.Literal["email-address"]

    class Config:
        frozen = True
        
        populate_by_name = True


class PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItem_RecordReference(
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemRecordReference
):
    attribute_type: typing_extensions.Literal["record-reference"]

    class Config:
        frozen = True
        
        populate_by_name = True


class PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItem_Interaction(
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemInteraction
):
    attribute_type: typing_extensions.Literal["interaction"]

    class Config:
        frozen = True
        
        populate_by_name = True


class PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItem_Location(
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemLocation
):
    attribute_type: typing_extensions.Literal["location"]

    class Config:
        frozen = True
        
        populate_by_name = True


class PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItem_Number(
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemNumber
):
    attribute_type: typing_extensions.Literal["number"]

    class Config:
        frozen = True
        
        populate_by_name = True


class PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItem_PersonalName(
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemPersonalName
):
    attribute_type: typing_extensions.Literal["personal-name"]

    class Config:
        frozen = True
        
        populate_by_name = True


class PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItem_PhoneNumber(
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemPhoneNumber
):
    attribute_type: typing_extensions.Literal["phone-number"]

    class Config:
        frozen = True
        
        populate_by_name = True


class PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItem_Status(
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemStatus
):
    attribute_type: typing_extensions.Literal["status"]

    class Config:
        frozen = True
        
        populate_by_name = True


class PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItem_Rating(
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemRating
):
    attribute_type: typing_extensions.Literal["rating"]

    class Config:
        frozen = True
        
        populate_by_name = True


class PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItem_Select(
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemSelect
):
    attribute_type: typing_extensions.Literal["select"]

    class Config:
        frozen = True
        
        populate_by_name = True


class PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItem_Text(
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemText
):
    attribute_type: typing_extensions.Literal["text"]

    class Config:
        frozen = True
        
        populate_by_name = True


class PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItem_Timestamp(
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemTimestamp
):
    attribute_type: typing_extensions.Literal["timestamp"]

    class Config:
        frozen = True
        
        populate_by_name = True


PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItem = typing.Union[
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItem_ActorReference,
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItem_Checkbox,
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItem_Currency,
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItem_Date,
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItem_Domain,
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItem_EmailAddress,
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItem_RecordReference,
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItem_Interaction,
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItem_Location,
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItem_Number,
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItem_PersonalName,
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItem_PhoneNumber,
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItem_Status,
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItem_Rating,
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItem_Select,
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItem_Text,
    PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItem_Timestamp,
]
