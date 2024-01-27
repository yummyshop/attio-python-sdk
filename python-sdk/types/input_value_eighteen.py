# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic.v1 as pydantic

from ..core.datetime_utils import serialize_datetime


class InputValueEighteen(pydantic.BaseModel):
    value: str = pydantic.Field(
        description='A timestamp value represents a single, universal moment in time using an ISO 8601 formatted string. This means that a timestamp consists of a date, a time (with nanosecond precision), and a time zone. Attio will coerce timestamps which do not provide full nanosecond precision and UTC is assumed if no time zone is provided. For example, "2023", "2023-01", "2023-01-02", "2023-01-02T13:00", "2023-01-02T13:00:00", and "2023-01-02T13:00:00.000000000" will all be coerced to "2023-01-02T13:00:00.000000000Z". Timestamps are always returned in UTC. For example, writing a timestamp value using the string "2023-01-02T13:00:00.000000000+02:00" will result in the value "2023-01-02T11:00:00.000000000Z" being returned.'
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
