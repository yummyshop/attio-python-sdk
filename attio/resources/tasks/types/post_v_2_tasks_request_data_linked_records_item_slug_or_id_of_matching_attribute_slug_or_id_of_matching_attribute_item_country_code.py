# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic as pydantic

from ....core.datetime_utils import serialize_datetime
from .post_v_2_tasks_request_data_linked_records_item_slug_or_id_of_matching_attribute_slug_or_id_of_matching_attribute_item_country_code_country_code import (
    PostV2TasksRequestDataLinkedRecordsItemSlugOrIdOfMatchingAttributeSlugOrIdOfMatchingAttributeItemCountryCodeCountryCode,
)


class PostV2TasksRequestDataLinkedRecordsItemSlugOrIdOfMatchingAttributeSlugOrIdOfMatchingAttributeItemCountryCode(
    pydantic.BaseModel
):
    original_phone_number: typing.Optional[str] = pydantic.Field(
        description="The raw, original phone number, as inputted."
    )
    country_code: typing.Optional[
        PostV2TasksRequestDataLinkedRecordsItemSlugOrIdOfMatchingAttributeSlugOrIdOfMatchingAttributeItemCountryCodeCountryCode
    ] = pydantic.Field(
        description="The ISO 3166-1 alpha-2 country code representing the country that this phone number belongs to."
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        
        json_encoders = {dt.datetime: serialize_datetime}
