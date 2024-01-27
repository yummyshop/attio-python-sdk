# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .patch_v_2_webhooks_webhook_id_response_data_subscriptions_item_filter_or_or_item_equals import (
    PatchV2WebhooksWebhookIdResponseDataSubscriptionsItemFilterOrOrItemEquals,
)
from .patch_v_2_webhooks_webhook_id_response_data_subscriptions_item_filter_or_or_item_not_equals import (
    PatchV2WebhooksWebhookIdResponseDataSubscriptionsItemFilterOrOrItemNotEquals,
)


class PatchV2WebhooksWebhookIdResponseDataSubscriptionsItemFilterOrOrItem_Equals(
    PatchV2WebhooksWebhookIdResponseDataSubscriptionsItemFilterOrOrItemEquals
):
    operator: typing_extensions.Literal["equals"]

    class Config:
        frozen = True
        
        allow_population_by_field_name = True


class PatchV2WebhooksWebhookIdResponseDataSubscriptionsItemFilterOrOrItem_NotEquals(
    PatchV2WebhooksWebhookIdResponseDataSubscriptionsItemFilterOrOrItemNotEquals
):
    operator: typing_extensions.Literal["not_equals"]

    class Config:
        frozen = True
        
        allow_population_by_field_name = True


PatchV2WebhooksWebhookIdResponseDataSubscriptionsItemFilterOrOrItem = typing.Union[
    PatchV2WebhooksWebhookIdResponseDataSubscriptionsItemFilterOrOrItem_Equals,
    PatchV2WebhooksWebhookIdResponseDataSubscriptionsItemFilterOrOrItem_NotEquals,
]
