# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic as pydantic

from ....core.datetime_utils import serialize_datetime
from .post_v_2_target_identifier_attributes_request_data_config_currency import (
    PostV2TargetIdentifierAttributesRequestDataConfigCurrency,
)
from .post_v_2_target_identifier_attributes_request_data_config_record_reference import (
    PostV2TargetIdentifierAttributesRequestDataConfigRecordReference,
)


class PostV2TargetIdentifierAttributesRequestDataConfig(pydantic.BaseModel):
    currency: typing.Optional[PostV2TargetIdentifierAttributesRequestDataConfigCurrency] = pydantic.Field(
        description='Configuration available for attributes of type "currency".'
    )
    record_reference: typing.Optional[
        PostV2TargetIdentifierAttributesRequestDataConfigRecordReference
    ] = pydantic.Field(description='Configuration available for attributes of type "record-reference".')

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
