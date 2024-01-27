# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostV2WebhooksResponseDataStatus(str, enum.Enum):
    """
    The state of the webhook. Webhooks marked as active and degraded will receive events, inactive ones will not. If a webhook remains in the degraded state for 7 days, it will be marked inactive.
    """

    ACTIVE = "active"
    DEGRADED = "degraded"
    INACTIVE = "inactive"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        degraded: typing.Callable[[], T_Result],
        inactive: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostV2WebhooksResponseDataStatus.ACTIVE:
            return active()
        if self is PostV2WebhooksResponseDataStatus.DEGRADED:
            return degraded()
        if self is PostV2WebhooksResponseDataStatus.INACTIVE:
            return inactive()