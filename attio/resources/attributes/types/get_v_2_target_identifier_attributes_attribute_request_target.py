# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetV2TargetIdentifierAttributesAttributeRequestTarget(str, enum.Enum):
    """
    Whether the attribute is on an object or a list.
    """

    OBJECTS = "objects"
    LISTS = "lists"

    def visit(self, objects: typing.Callable[[], T_Result], lists: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetV2TargetIdentifierAttributesAttributeRequestTarget.OBJECTS:
            return objects()
        if self is GetV2TargetIdentifierAttributesAttributeRequestTarget.LISTS:
            return lists()
