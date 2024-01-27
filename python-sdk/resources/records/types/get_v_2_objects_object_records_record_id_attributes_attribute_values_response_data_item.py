# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .get_v_2_objects_object_records_record_id_attributes_attribute_values_response_data_item_actor_reference import (
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemActorReference,
)
from .get_v_2_objects_object_records_record_id_attributes_attribute_values_response_data_item_checkbox import (
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemCheckbox,
)
from .get_v_2_objects_object_records_record_id_attributes_attribute_values_response_data_item_currency import (
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemCurrency,
)
from .get_v_2_objects_object_records_record_id_attributes_attribute_values_response_data_item_date import (
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemDate,
)
from .get_v_2_objects_object_records_record_id_attributes_attribute_values_response_data_item_domain import (
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemDomain,
)
from .get_v_2_objects_object_records_record_id_attributes_attribute_values_response_data_item_email_address import (
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemEmailAddress,
)
from .get_v_2_objects_object_records_record_id_attributes_attribute_values_response_data_item_interaction import (
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemInteraction,
)
from .get_v_2_objects_object_records_record_id_attributes_attribute_values_response_data_item_location import (
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemLocation,
)
from .get_v_2_objects_object_records_record_id_attributes_attribute_values_response_data_item_number import (
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemNumber,
)
from .get_v_2_objects_object_records_record_id_attributes_attribute_values_response_data_item_personal_name import (
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemPersonalName,
)
from .get_v_2_objects_object_records_record_id_attributes_attribute_values_response_data_item_phone_number import (
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemPhoneNumber,
)
from .get_v_2_objects_object_records_record_id_attributes_attribute_values_response_data_item_rating import (
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemRating,
)
from .get_v_2_objects_object_records_record_id_attributes_attribute_values_response_data_item_record_reference import (
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemRecordReference,
)
from .get_v_2_objects_object_records_record_id_attributes_attribute_values_response_data_item_select import (
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemSelect,
)
from .get_v_2_objects_object_records_record_id_attributes_attribute_values_response_data_item_status import (
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemStatus,
)
from .get_v_2_objects_object_records_record_id_attributes_attribute_values_response_data_item_text import (
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemText,
)
from .get_v_2_objects_object_records_record_id_attributes_attribute_values_response_data_item_timestamp import (
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemTimestamp,
)


class GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItem_ActorReference(
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemActorReference
):
    attribute_type: typing_extensions.Literal["actor-reference"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItem_Checkbox(
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemCheckbox
):
    attribute_type: typing_extensions.Literal["checkbox"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItem_Currency(
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemCurrency
):
    attribute_type: typing_extensions.Literal["currency"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItem_Date(
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemDate
):
    attribute_type: typing_extensions.Literal["date"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItem_Domain(
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemDomain
):
    attribute_type: typing_extensions.Literal["domain"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItem_EmailAddress(
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemEmailAddress
):
    attribute_type: typing_extensions.Literal["email-address"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItem_RecordReference(
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemRecordReference
):
    attribute_type: typing_extensions.Literal["record-reference"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItem_Interaction(
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemInteraction
):
    attribute_type: typing_extensions.Literal["interaction"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItem_Location(
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemLocation
):
    attribute_type: typing_extensions.Literal["location"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItem_Number(
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemNumber
):
    attribute_type: typing_extensions.Literal["number"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItem_PersonalName(
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemPersonalName
):
    attribute_type: typing_extensions.Literal["personal-name"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItem_PhoneNumber(
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemPhoneNumber
):
    attribute_type: typing_extensions.Literal["phone-number"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItem_Status(
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemStatus
):
    attribute_type: typing_extensions.Literal["status"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItem_Rating(
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemRating
):
    attribute_type: typing_extensions.Literal["rating"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItem_Select(
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemSelect
):
    attribute_type: typing_extensions.Literal["select"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItem_Text(
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemText
):
    attribute_type: typing_extensions.Literal["text"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItem_Timestamp(
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemTimestamp
):
    attribute_type: typing_extensions.Literal["timestamp"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItem = typing.Union[
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItem_ActorReference,
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItem_Checkbox,
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItem_Currency,
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItem_Date,
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItem_Domain,
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItem_EmailAddress,
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItem_RecordReference,
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItem_Interaction,
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItem_Location,
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItem_Number,
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItem_PersonalName,
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItem_PhoneNumber,
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItem_Status,
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItem_Rating,
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItem_Select,
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItem_Text,
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItem_Timestamp,
]
