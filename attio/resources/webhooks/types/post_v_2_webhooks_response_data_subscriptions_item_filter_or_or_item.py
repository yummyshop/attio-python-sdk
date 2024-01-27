# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .post_v_2_webhooks_response_data_subscriptions_item_filter_or_or_item_equals import (
    PostV2WebhooksResponseDataSubscriptionsItemFilterOrOrItemEquals,
)
from .post_v_2_webhooks_response_data_subscriptions_item_filter_or_or_item_not_equals import (
    PostV2WebhooksResponseDataSubscriptionsItemFilterOrOrItemNotEquals,
)


class PostV2WebhooksResponseDataSubscriptionsItemFilterOrOrItem_Equals(
    PostV2WebhooksResponseDataSubscriptionsItemFilterOrOrItemEquals
):
    operator: typing_extensions.Literal["equals"]

    class Config:
        frozen = True
        
        populate_by_name = True


class PostV2WebhooksResponseDataSubscriptionsItemFilterOrOrItem_NotEquals(
    PostV2WebhooksResponseDataSubscriptionsItemFilterOrOrItemNotEquals
):
    operator: typing_extensions.Literal["not_equals"]

    class Config:
        frozen = True
        
        populate_by_name = True


PostV2WebhooksResponseDataSubscriptionsItemFilterOrOrItem = typing.Union[
    PostV2WebhooksResponseDataSubscriptionsItemFilterOrOrItem_Equals,
    PostV2WebhooksResponseDataSubscriptionsItemFilterOrOrItem_NotEquals,
]
