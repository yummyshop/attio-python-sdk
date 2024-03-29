# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ListWorkspaceMemberAccessItemLevel(str, enum.Enum):
    """
    The level of access to the list.
    """

    FULL_ACCESS = "full-access"
    READ_AND_WRITE = "read-and-write"
    READ_ONLY = "read-only"

    def visit(
        self,
        full_access: typing.Callable[[], T_Result],
        read_and_write: typing.Callable[[], T_Result],
        read_only: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListWorkspaceMemberAccessItemLevel.FULL_ACCESS:
            return full_access()
        if self is ListWorkspaceMemberAccessItemLevel.READ_AND_WRITE:
            return read_and_write()
        if self is ListWorkspaceMemberAccessItemLevel.READ_ONLY:
            return read_only()
