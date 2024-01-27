# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic.v1 as pydantic

from ....core.datetime_utils import serialize_datetime
from .patch_v_2_objects_object_records_record_id_response_data_id import (
    PatchV2ObjectsObjectRecordsRecordIdResponseDataId,
)
from .patch_v_2_objects_object_records_record_id_response_data_values_value_item import (
    PatchV2ObjectsObjectRecordsRecordIdResponseDataValuesValueItem,
)


class PatchV2ObjectsObjectRecordsRecordIdResponseData(pydantic.BaseModel):
    id: PatchV2ObjectsObjectRecordsRecordIdResponseDataId
    created_at: str = pydantic.Field(description="When this record was created.")
    values: typing.Dict[
        str, typing.List[PatchV2ObjectsObjectRecordsRecordIdResponseDataValuesValueItem]
    ] = pydantic.Field(
        description="A record type with an attribute `api_slug` as the key, and an array of value objects as the values."
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
