# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostV2TargetIdentifierAttributesRequestDataType(str, enum.Enum):
    """
    The type of the attribute. This value affects the possible `config` values. Attributes of type "status" are not supported on objects.
    """

    TEXT = "text"
    NUMBER = "number"
    CHECKBOX = "checkbox"
    CURRENCY = "currency"
    DATE = "date"
    TIMESTAMP = "timestamp"
    RATING = "rating"
    STATUS = "status"
    SELECT = "select"
    RECORD_REFERENCE = "record-reference"
    ACTOR_REFERENCE = "actor-reference"
    LOCATION = "location"
    DOMAIN = "domain"
    EMAIL_ADDRESS = "email-address"
    PHONE_NUMBER = "phone-number"

    def visit(
        self,
        text: typing.Callable[[], T_Result],
        number: typing.Callable[[], T_Result],
        checkbox: typing.Callable[[], T_Result],
        currency: typing.Callable[[], T_Result],
        date: typing.Callable[[], T_Result],
        timestamp: typing.Callable[[], T_Result],
        rating: typing.Callable[[], T_Result],
        status: typing.Callable[[], T_Result],
        select: typing.Callable[[], T_Result],
        record_reference: typing.Callable[[], T_Result],
        actor_reference: typing.Callable[[], T_Result],
        location: typing.Callable[[], T_Result],
        domain: typing.Callable[[], T_Result],
        email_address: typing.Callable[[], T_Result],
        phone_number: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostV2TargetIdentifierAttributesRequestDataType.TEXT:
            return text()
        if self is PostV2TargetIdentifierAttributesRequestDataType.NUMBER:
            return number()
        if self is PostV2TargetIdentifierAttributesRequestDataType.CHECKBOX:
            return checkbox()
        if self is PostV2TargetIdentifierAttributesRequestDataType.CURRENCY:
            return currency()
        if self is PostV2TargetIdentifierAttributesRequestDataType.DATE:
            return date()
        if self is PostV2TargetIdentifierAttributesRequestDataType.TIMESTAMP:
            return timestamp()
        if self is PostV2TargetIdentifierAttributesRequestDataType.RATING:
            return rating()
        if self is PostV2TargetIdentifierAttributesRequestDataType.STATUS:
            return status()
        if self is PostV2TargetIdentifierAttributesRequestDataType.SELECT:
            return select()
        if self is PostV2TargetIdentifierAttributesRequestDataType.RECORD_REFERENCE:
            return record_reference()
        if self is PostV2TargetIdentifierAttributesRequestDataType.ACTOR_REFERENCE:
            return actor_reference()
        if self is PostV2TargetIdentifierAttributesRequestDataType.LOCATION:
            return location()
        if self is PostV2TargetIdentifierAttributesRequestDataType.DOMAIN:
            return domain()
        if self is PostV2TargetIdentifierAttributesRequestDataType.EMAIL_ADDRESS:
            return email_address()
        if self is PostV2TargetIdentifierAttributesRequestDataType.PHONE_NUMBER:
            return phone_number()
