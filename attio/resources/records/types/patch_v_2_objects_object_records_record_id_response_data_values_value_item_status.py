# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic as pydantic

from ....core.datetime_utils import serialize_datetime
from ....types.status import Status
from .patch_v_2_objects_object_records_record_id_response_data_values_value_item_status_created_by_actor import (
    PatchV2ObjectsObjectRecordsRecordIdResponseDataValuesValueItemStatusCreatedByActor,
)


class PatchV2ObjectsObjectRecordsRecordIdResponseDataValuesValueItemStatus(pydantic.BaseModel):
    active_from: dt.datetime = pydantic.Field(
        description='The point in time at which this value was made "active". `active_from` can be considered roughly analogous to `created_at`.'
    )
    active_until: typing.Optional[dt.datetime] = pydantic.Field(
        description="The point in time at which this value was deactivated. If `null`, the value is active."
    )
    created_by_actor: PatchV2ObjectsObjectRecordsRecordIdResponseDataValuesValueItemStatusCreatedByActor = (
        pydantic.Field(description="The actor that created this value.")
    )
    status: Status

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        
        json_encoders = {dt.datetime: serialize_datetime}
