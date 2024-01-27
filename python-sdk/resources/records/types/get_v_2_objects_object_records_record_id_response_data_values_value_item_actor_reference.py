# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic.v1 as pydantic

from ....core.datetime_utils import serialize_datetime
from .get_v_2_objects_object_records_record_id_response_data_values_value_item_actor_reference_created_by_actor import (
    GetV2ObjectsObjectRecordsRecordIdResponseDataValuesValueItemActorReferenceCreatedByActor,
)
from .get_v_2_objects_object_records_record_id_response_data_values_value_item_actor_reference_referenced_actor_type import (
    GetV2ObjectsObjectRecordsRecordIdResponseDataValuesValueItemActorReferenceReferencedActorType,
)


class GetV2ObjectsObjectRecordsRecordIdResponseDataValuesValueItemActorReference(pydantic.BaseModel):
    active_from: dt.datetime = pydantic.Field(
        description='The point in time at which this value was made "active". `active_from` can be considered roughly analogous to `created_at`.'
    )
    active_until: typing.Optional[dt.datetime] = pydantic.Field(
        description="The point in time at which this value was deactivated. If `null`, the value is active."
    )
    created_by_actor: GetV2ObjectsObjectRecordsRecordIdResponseDataValuesValueItemActorReferenceCreatedByActor = (
        pydantic.Field(description="The actor that created this value.")
    )
    referenced_actor_type: GetV2ObjectsObjectRecordsRecordIdResponseDataValuesValueItemActorReferenceReferencedActorType = pydantic.Field(
        description="The type of the referenced actor. [Read more information on actor types here](/docs/actors)."
    )
    referenced_actor_id: typing.Optional[str] = pydantic.Field(description="The ID of the referenced actor.")

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
