# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemInteractionOwnerActorType(str, enum.Enum):
    """
    The type of actor. [Read more information on actor types here](/docs/actors).
    """

    API_TOKEN = "api-token"
    WORKSPACE_MEMBER = "workspace-member"
    SYSTEM = "system"

    def visit(
        self,
        api_token: typing.Callable[[], T_Result],
        workspace_member: typing.Callable[[], T_Result],
        system: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemInteractionOwnerActorType.API_TOKEN:
            return api_token()
        if (
            self
            is PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemInteractionOwnerActorType.WORKSPACE_MEMBER
        ):
            return workspace_member()
        if self is PostV2ListsListEntriesQueryResponseDataItemEntryValuesValueItemInteractionOwnerActorType.SYSTEM:
            return system()
