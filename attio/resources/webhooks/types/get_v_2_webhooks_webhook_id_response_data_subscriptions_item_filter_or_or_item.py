# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .get_v_2_webhooks_webhook_id_response_data_subscriptions_item_filter_or_or_item_equals import (
    GetV2WebhooksWebhookIdResponseDataSubscriptionsItemFilterOrOrItemEquals,
)
from .get_v_2_webhooks_webhook_id_response_data_subscriptions_item_filter_or_or_item_not_equals import (
    GetV2WebhooksWebhookIdResponseDataSubscriptionsItemFilterOrOrItemNotEquals,
)


class GetV2WebhooksWebhookIdResponseDataSubscriptionsItemFilterOrOrItem_Equals(
    GetV2WebhooksWebhookIdResponseDataSubscriptionsItemFilterOrOrItemEquals
):
    operator: typing_extensions.Literal["equals"]

    class Config:
        frozen = True
        
        populate_by_name = True


class GetV2WebhooksWebhookIdResponseDataSubscriptionsItemFilterOrOrItem_NotEquals(
    GetV2WebhooksWebhookIdResponseDataSubscriptionsItemFilterOrOrItemNotEquals
):
    operator: typing_extensions.Literal["not_equals"]

    class Config:
        frozen = True
        
        populate_by_name = True


GetV2WebhooksWebhookIdResponseDataSubscriptionsItemFilterOrOrItem = typing.Union[
    GetV2WebhooksWebhookIdResponseDataSubscriptionsItemFilterOrOrItem_Equals,
    GetV2WebhooksWebhookIdResponseDataSubscriptionsItemFilterOrOrItem_NotEquals,
]
