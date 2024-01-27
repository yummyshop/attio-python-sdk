# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemInteractionInteractionType(str, enum.Enum):
    """
    The type of interaction e.g. calendar or email.
    """

    EMAIL = "email"
    CALENDAR_EVENT = "calendar-event"

    def visit(self, email: typing.Callable[[], T_Result], calendar_event: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemInteractionInteractionType.EMAIL:
            return email()
        if (
            self
            is PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemInteractionInteractionType.CALENDAR_EVENT
        ):
            return calendar_event()
