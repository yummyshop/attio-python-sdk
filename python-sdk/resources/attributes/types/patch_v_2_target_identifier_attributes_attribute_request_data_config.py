# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic.v1 as pydantic

from ....core.datetime_utils import serialize_datetime
from .patch_v_2_target_identifier_attributes_attribute_request_data_config_currency import (
    PatchV2TargetIdentifierAttributesAttributeRequestDataConfigCurrency,
)
from .patch_v_2_target_identifier_attributes_attribute_request_data_config_record_reference import (
    PatchV2TargetIdentifierAttributesAttributeRequestDataConfigRecordReference,
)


class PatchV2TargetIdentifierAttributesAttributeRequestDataConfig(pydantic.BaseModel):
    """
    Additional, type-dependent configuration for the attribute.
    """

    currency: typing.Optional[PatchV2TargetIdentifierAttributesAttributeRequestDataConfigCurrency] = pydantic.Field(
        description='Configuration available for attributes of type "currency".'
    )
    record_reference: typing.Optional[
        PatchV2TargetIdentifierAttributesAttributeRequestDataConfigRecordReference
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
