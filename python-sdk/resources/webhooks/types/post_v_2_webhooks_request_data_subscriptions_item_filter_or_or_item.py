# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .post_v_2_webhooks_request_data_subscriptions_item_filter_or_or_item_equals import (
    PostV2WebhooksRequestDataSubscriptionsItemFilterOrOrItemEquals,
)
from .post_v_2_webhooks_request_data_subscriptions_item_filter_or_or_item_not_equals import (
    PostV2WebhooksRequestDataSubscriptionsItemFilterOrOrItemNotEquals,
)


class PostV2WebhooksRequestDataSubscriptionsItemFilterOrOrItem_Equals(
    PostV2WebhooksRequestDataSubscriptionsItemFilterOrOrItemEquals
):
    operator: typing_extensions.Literal["equals"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2WebhooksRequestDataSubscriptionsItemFilterOrOrItem_NotEquals(
    PostV2WebhooksRequestDataSubscriptionsItemFilterOrOrItemNotEquals
):
    operator: typing_extensions.Literal["not_equals"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


PostV2WebhooksRequestDataSubscriptionsItemFilterOrOrItem = typing.Union[
    PostV2WebhooksRequestDataSubscriptionsItemFilterOrOrItem_Equals,
    PostV2WebhooksRequestDataSubscriptionsItemFilterOrOrItem_NotEquals,
]
