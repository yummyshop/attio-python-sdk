# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic as pydantic

from ....core.datetime_utils import serialize_datetime
from .patch_v_2_target_identifier_attributes_attribute_request_data_config import (
    PatchV2TargetIdentifierAttributesAttributeRequestDataConfig,
)
from .patch_v_2_target_identifier_attributes_attribute_request_data_default_value import (
    PatchV2TargetIdentifierAttributesAttributeRequestDataDefaultValue,
)


class PatchV2TargetIdentifierAttributesAttributeRequestData(pydantic.BaseModel):
    title: typing.Optional[str] = pydantic.Field(
        description="The name of the attribute. The title will be visible across Attio's UI."
    )
    description: typing.Optional[str] = pydantic.Field(description="A text description for the attribute.")
    api_slug: typing.Optional[str] = pydantic.Field(
        description="A unique, human-readable slug to access the attribute through URLs and API calls. Formatted in snake case."
    )
    is_required: typing.Optional[bool] = pydantic.Field(
        description="When `is_required` is `true`, new records/entries must have a value for this attribute. If `false`, values may be `null`. This value does not affect existing data and you do not need to backfill `null` values if changing `is_required` from `false` to `true`."
    )
    default_value: typing.Optional[PatchV2TargetIdentifierAttributesAttributeRequestDataDefaultValue] = pydantic.Field(
        description="The default value for this attribute. Static values are used to directly populate values using their contents. Dynamic values are used to lookup data at the point of creation. For example, you could use a dynamic value to insert a value for the currently logged in user. Which default values are available is dependent on the type of the attribute. Default values are not currently supported on people or company objects."
    )
    config: typing.Optional[PatchV2TargetIdentifierAttributesAttributeRequestDataConfig] = pydantic.Field(
        description="Additional, type-dependent configuration for the attribute."
    )
    is_archived: typing.Optional[bool] = pydantic.Field(
        description="Whether the attribute has been archived or not. See our [archiving guide](/docs/archiving-vs-deleting) for more information on archiving."
    )

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