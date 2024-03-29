# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostV2ListsRequestDataWorkspaceAccess(str, enum.Enum):
    """
    The level of access granted to all members of the workspace for this list. Pass `null` to keep the list private and only grant access to specific workspace members.
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
        if self is PostV2ListsRequestDataWorkspaceAccess.FULL_ACCESS:
            return full_access()
        if self is PostV2ListsRequestDataWorkspaceAccess.READ_AND_WRITE:
            return read_and_write()
        if self is PostV2ListsRequestDataWorkspaceAccess.READ_ONLY:
            return read_only()
