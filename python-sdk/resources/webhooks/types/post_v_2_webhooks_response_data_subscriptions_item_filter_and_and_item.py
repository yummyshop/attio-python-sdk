# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .post_v_2_webhooks_response_data_subscriptions_item_filter_and_and_item_equals import (
    PostV2WebhooksResponseDataSubscriptionsItemFilterAndAndItemEquals,
)
from .post_v_2_webhooks_response_data_subscriptions_item_filter_and_and_item_not_equals import (
    PostV2WebhooksResponseDataSubscriptionsItemFilterAndAndItemNotEquals,
)


class PostV2WebhooksResponseDataSubscriptionsItemFilterAndAndItem_Equals(
    PostV2WebhooksResponseDataSubscriptionsItemFilterAndAndItemEquals
):
    operator: typing_extensions.Literal["equals"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PostV2WebhooksResponseDataSubscriptionsItemFilterAndAndItem_NotEquals(
    PostV2WebhooksResponseDataSubscriptionsItemFilterAndAndItemNotEquals
):
    operator: typing_extensions.Literal["not_equals"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


PostV2WebhooksResponseDataSubscriptionsItemFilterAndAndItem = typing.Union[
    PostV2WebhooksResponseDataSubscriptionsItemFilterAndAndItem_Equals,
    PostV2WebhooksResponseDataSubscriptionsItemFilterAndAndItem_NotEquals,
]