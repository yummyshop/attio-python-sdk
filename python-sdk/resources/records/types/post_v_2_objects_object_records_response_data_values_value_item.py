# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .post_v_2_objects_object_records_response_data_values_value_item_actor_reference import (
    PostV2ObjectsObjectRecordsResponseDataValuesValueItemActorReference,
)
from .post_v_2_objects_object_records_response_data_values_value_item_checkbox import (
    PostV2ObjectsObjectRecordsResponseDataValuesValueItemCheckbox,
)
from .post_v_2_objects_object_records_response_data_values_value_item_currency import (
    PostV2ObjectsObjectRecordsResponseDataValuesValueItemCurrency,
)
from .post_v_2_objects_object_records_response_data_values_value_item_date import (
    PostV2ObjectsObjectRecordsResponseDataValuesValueItemDate,
)
from .post_v_2_objects_object_records_response_data_values_value_item_domain import (
    PostV2ObjectsObjectRecordsResponseDataValuesValueItemDomain,
)
from .post_v_2_objects_object_records_response_data_values_value_item_email_address import (
    PostV2ObjectsObjectRecordsResponseDataValuesValueItemEmailAddress,
)
from .post_v_2_objects_object_records_response_data_values_value_item_interaction import (
    PostV2ObjectsObjectRecordsResponseDataValuesValueItemInteraction,
)
from .post_v_2_objects_object_records_response_data_values_value_item_location import (
    PostV2ObjectsObjectRecordsResponseDataValuesValueItemLocation,
)
from .post_v_2_objects_object_records_response_data_values_value_item_number import (
    PostV2ObjectsObjectRecordsResponseDataValuesValueItemNumber,
)
from .post_v_2_objects_object_records_response_data_values_value_item_personal_name import (
    PostV2ObjectsObjectRecordsResponseDataValuesValueItemPersonalName,
)
from .post_v_2_objects_object_records_response_data_values_value_item_phone_number import (
    PostV2ObjectsObjectRecordsResponseDataValuesValueItemPhoneNumber,
)
from .post_v_2_objects_object_records_response_data_values_value_item_rating import (
    PostV2ObjectsObjectRecordsResponseDataValuesValueItemRating,
)
from .post_v_2_objects_object_records_response_data_values_value_item_record_reference import (
    PostV2ObjectsObjectRecordsResponseDataValuesValueItemRecordReference,
)
from .post_v_2_objects_object_records_response_data_values_value_item_select import (
    PostV2ObjectsObjectRecordsResponseDataValuesValueItemSelect,
)
from .post_v_2_objects_object_records_response_data_values_value_item_status import (
    PostV2ObjectsObjectRecordsResponseDataValuesValueItemStatus,
)
from .post_v_2_objects_object_records_response_data_values_value_item_text import (
    PostV2ObjectsObjectRecordsResponseDataValuesValueItemText,
)
from .post_v_2_objects_object_records_response_data_values_value_item_timestamp import (
    PostV2ObjectsObjectRecordsResponseDataValuesValueItemTimestamp,
)


class PostV2ObjectsObjectRecordsResponseDataValuesValueItem_ActorReference(
    PostV2ObjectsObjectRecordsResponseDataValuesValueItemActorReference
):
    attribute_type: typing_extensions.Literal["actor-reference"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ObjectsObjectRecordsResponseDataValuesValueItem_Checkbox(
    PostV2ObjectsObjectRecordsResponseDataValuesValueItemCheckbox
):
    attribute_type: typing_extensions.Literal["checkbox"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ObjectsObjectRecordsResponseDataValuesValueItem_Currency(
    PostV2ObjectsObjectRecordsResponseDataValuesValueItemCurrency
):
    attribute_type: typing_extensions.Literal["currency"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ObjectsObjectRecordsResponseDataValuesValueItem_Date(
    PostV2ObjectsObjectRecordsResponseDataValuesValueItemDate
):
    attribute_type: typing_extensions.Literal["date"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ObjectsObjectRecordsResponseDataValuesValueItem_Domain(
    PostV2ObjectsObjectRecordsResponseDataValuesValueItemDomain
):
    attribute_type: typing_extensions.Literal["domain"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ObjectsObjectRecordsResponseDataValuesValueItem_EmailAddress(
    PostV2ObjectsObjectRecordsResponseDataValuesValueItemEmailAddress
):
    attribute_type: typing_extensions.Literal["email-address"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ObjectsObjectRecordsResponseDataValuesValueItem_RecordReference(
    PostV2ObjectsObjectRecordsResponseDataValuesValueItemRecordReference
):
    attribute_type: typing_extensions.Literal["record-reference"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ObjectsObjectRecordsResponseDataValuesValueItem_Interaction(
    PostV2ObjectsObjectRecordsResponseDataValuesValueItemInteraction
):
    attribute_type: typing_extensions.Literal["interaction"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ObjectsObjectRecordsResponseDataValuesValueItem_Location(
    PostV2ObjectsObjectRecordsResponseDataValuesValueItemLocation
):
    attribute_type: typing_extensions.Literal["location"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ObjectsObjectRecordsResponseDataValuesValueItem_Number(
    PostV2ObjectsObjectRecordsResponseDataValuesValueItemNumber
):
    attribute_type: typing_extensions.Literal["number"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ObjectsObjectRecordsResponseDataValuesValueItem_PersonalName(
    PostV2ObjectsObjectRecordsResponseDataValuesValueItemPersonalName
):
    attribute_type: typing_extensions.Literal["personal-name"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ObjectsObjectRecordsResponseDataValuesValueItem_PhoneNumber(
    PostV2ObjectsObjectRecordsResponseDataValuesValueItemPhoneNumber
):
    attribute_type: typing_extensions.Literal["phone-number"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ObjectsObjectRecordsResponseDataValuesValueItem_Status(
    PostV2ObjectsObjectRecordsResponseDataValuesValueItemStatus
):
    attribute_type: typing_extensions.Literal["status"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ObjectsObjectRecordsResponseDataValuesValueItem_Rating(
    PostV2ObjectsObjectRecordsResponseDataValuesValueItemRating
):
    attribute_type: typing_extensions.Literal["rating"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ObjectsObjectRecordsResponseDataValuesValueItem_Select(
    PostV2ObjectsObjectRecordsResponseDataValuesValueItemSelect
):
    attribute_type: typing_extensions.Literal["select"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ObjectsObjectRecordsResponseDataValuesValueItem_Text(
    PostV2ObjectsObjectRecordsResponseDataValuesValueItemText
):
    attribute_type: typing_extensions.Literal["text"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2ObjectsObjectRecordsResponseDataValuesValueItem_Timestamp(
    PostV2ObjectsObjectRecordsResponseDataValuesValueItemTimestamp
):
    attribute_type: typing_extensions.Literal["timestamp"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


PostV2ObjectsObjectRecordsResponseDataValuesValueItem = typing.Union[
    PostV2ObjectsObjectRecordsResponseDataValuesValueItem_ActorReference,
    PostV2ObjectsObjectRecordsResponseDataValuesValueItem_Checkbox,
    PostV2ObjectsObjectRecordsResponseDataValuesValueItem_Currency,
    PostV2ObjectsObjectRecordsResponseDataValuesValueItem_Date,
    PostV2ObjectsObjectRecordsResponseDataValuesValueItem_Domain,
    PostV2ObjectsObjectRecordsResponseDataValuesValueItem_EmailAddress,
    PostV2ObjectsObjectRecordsResponseDataValuesValueItem_RecordReference,
    PostV2ObjectsObjectRecordsResponseDataValuesValueItem_Interaction,
    PostV2ObjectsObjectRecordsResponseDataValuesValueItem_Location,
    PostV2ObjectsObjectRecordsResponseDataValuesValueItem_Number,
    PostV2ObjectsObjectRecordsResponseDataValuesValueItem_PersonalName,
    PostV2ObjectsObjectRecordsResponseDataValuesValueItem_PhoneNumber,
    PostV2ObjectsObjectRecordsResponseDataValuesValueItem_Status,
    PostV2ObjectsObjectRecordsResponseDataValuesValueItem_Rating,
    PostV2ObjectsObjectRecordsResponseDataValuesValueItem_Select,
    PostV2ObjectsObjectRecordsResponseDataValuesValueItem_Text,
    PostV2ObjectsObjectRecordsResponseDataValuesValueItem_Timestamp,
]
