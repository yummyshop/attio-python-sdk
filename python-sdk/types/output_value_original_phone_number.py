# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic as pydantic
import typing_extensions

from ..core.datetime_utils import serialize_datetime
from .output_value_original_phone_number_country_code import OutputValueOriginalPhoneNumberCountryCode


class OutputValueOriginalPhoneNumber(pydantic.BaseModel):
    original_phone_number: str = pydantic.Field(description="The raw, original phone number, as inputted.")
    country_code: OutputValueOriginalPhoneNumberCountryCode = pydantic.Field(
        description="The ISO 3166-1 alpha-2 country code representing the country that this phone number belongs to."
    )
    phone_number: str
    attribute_type: typing_extensions.Literal["phone-number"]

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
