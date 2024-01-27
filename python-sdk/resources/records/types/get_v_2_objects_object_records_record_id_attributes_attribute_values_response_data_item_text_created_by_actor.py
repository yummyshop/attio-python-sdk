# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic.v1 as pydantic

from ....core.datetime_utils import serialize_datetime
from .get_v_2_objects_object_records_record_id_attributes_attribute_values_response_data_item_text_created_by_actor_type import (
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemTextCreatedByActorType,
)


class GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemTextCreatedByActor(pydantic.BaseModel):
    """
    The actor that created this value.
    """

    id: typing.Optional[str] = pydantic.Field(description="An ID to identify the actor.")
    type: typing.Optional[
        GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponseDataItemTextCreatedByActorType
    ] = pydantic.Field(description="The type of actor. [Read more information on actor types here](/docs/actors).")

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
