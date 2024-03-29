# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic as pydantic

from ....core.datetime_utils import serialize_datetime
from .get_v_2_webhooks_response_data_item_subscriptions_item_event_type import (
    GetV2WebhooksResponseDataItemSubscriptionsItemEventType,
)
from .get_v_2_webhooks_response_data_item_subscriptions_item_filter import (
    GetV2WebhooksResponseDataItemSubscriptionsItemFilter,
)


class GetV2WebhooksResponseDataItemSubscriptionsItem(pydantic.BaseModel):
    event_type: GetV2WebhooksResponseDataItemSubscriptionsItemEventType = pydantic.Field(
        description="Type of event the webhook is subscribed to."
    )
    filter: typing.Optional[GetV2WebhooksResponseDataItemSubscriptionsItemFilter] = pydantic.Field(
        description="Filters to determine whether the webhook event should be sent. If null, the filter always passes."
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        
        json_encoders = {dt.datetime: serialize_datetime}
