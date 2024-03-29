# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic as pydantic

from ....core.datetime_utils import serialize_datetime
from .patch_v_2_webhooks_webhook_id_response_data_id import PatchV2WebhooksWebhookIdResponseDataId
from .patch_v_2_webhooks_webhook_id_response_data_status import PatchV2WebhooksWebhookIdResponseDataStatus
from .patch_v_2_webhooks_webhook_id_response_data_subscriptions_item import (
    PatchV2WebhooksWebhookIdResponseDataSubscriptionsItem,
)


class PatchV2WebhooksWebhookIdResponseData(pydantic.BaseModel):
    target_url: str = pydantic.Field(description="URL where the webhook events will be delivered to.")
    subscriptions: typing.List[PatchV2WebhooksWebhookIdResponseDataSubscriptionsItem] = pydantic.Field(
        description="One or more events the webhook is subscribed to."
    )
    id: PatchV2WebhooksWebhookIdResponseDataId
    status: PatchV2WebhooksWebhookIdResponseDataStatus = pydantic.Field(
        description="The state of the webhook. Webhooks marked as active and degraded will receive events, inactive ones will not. If a webhook remains in the degraded state for 7 days, it will be marked inactive."
    )
    created_at: str = pydantic.Field(description="When the webhook was created.")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        
        json_encoders = {dt.datetime: serialize_datetime}
