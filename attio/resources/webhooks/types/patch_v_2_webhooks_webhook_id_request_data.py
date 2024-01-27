# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic as pydantic

from ....core.datetime_utils import serialize_datetime
from .patch_v_2_webhooks_webhook_id_request_data_subscriptions_item import (
    PatchV2WebhooksWebhookIdRequestDataSubscriptionsItem,
)


class PatchV2WebhooksWebhookIdRequestData(pydantic.BaseModel):
    target_url: typing.Optional[str] = pydantic.Field(description="URL where the webhook events will be delivered to.")
    subscriptions: typing.Optional[typing.List[PatchV2WebhooksWebhookIdRequestDataSubscriptionsItem]] = pydantic.Field(
        description="One or more events the webhook is subscribed to."
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
