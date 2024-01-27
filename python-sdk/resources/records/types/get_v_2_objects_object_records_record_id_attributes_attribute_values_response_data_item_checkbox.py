# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic as pydantic

from ....core.datetime_utils import serialize_datetime
from .get_v_2_objects_object_records_record_id_attributes_attribute_values_response_data_item_checkbox_created_by_actor import (
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemCheckboxCreatedByActor,
)


class GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemCheckbox(pydantic.BaseModel):
    active_from: dt.datetime = pydantic.Field(
        description='The point in time at which this value was made "active". `active_from` can be considered roughly analogous to `created_at`.'
    )
    active_until: typing.Optional[dt.datetime] = pydantic.Field(
        description="The point in time at which this value was deactivated. If `null`, the value is active."
    )
    created_by_actor: GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemCheckboxCreatedByActor = pydantic.Field(
        description="The actor that created this value."
    )
    value: bool = pydantic.Field(
        description="A boolean representing whether the checkbox is checked or not. The string values 'true' and 'false' are also accepted."
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
