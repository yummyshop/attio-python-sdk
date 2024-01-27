# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic as pydantic

from ....core.datetime_utils import serialize_datetime
from .post_v_2_webhooks_response_data_subscriptions_item_filter_or_or_item import (
    PostV2WebhooksResponseDataSubscriptionsItemFilterOrOrItem,
)


class PostV2WebhooksResponseDataSubscriptionsItemFilterOr(pydantic.BaseModel):
    or_: typing.List[PostV2WebhooksResponseDataSubscriptionsItemFilterOrOrItem] = pydantic.Field(alias="$or")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
