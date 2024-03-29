# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostV2TargetIdentifierAttributesAttributeStatusesRequestTarget(str, enum.Enum):
    """
    Whether the attribute is on an object or a list. Please note that company and person objects do not support status attributes at this time.
    """

    LISTS = "lists"
    OBJECTS = "objects"

    def visit(self, lists: typing.Callable[[], T_Result], objects: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostV2TargetIdentifierAttributesAttributeStatusesRequestTarget.LISTS:
            return lists()
        if self is PostV2TargetIdentifierAttributesAttributeStatusesRequestTarget.OBJECTS:
            return objects()
