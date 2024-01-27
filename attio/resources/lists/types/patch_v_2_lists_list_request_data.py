# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic as pydantic

from ....core.datetime_utils import serialize_datetime
from .patch_v_2_lists_list_request_data_workspace_access import PatchV2ListsListRequestDataWorkspaceAccess
from .patch_v_2_lists_list_request_data_workspace_member_access_item import (
    PatchV2ListsListRequestDataWorkspaceMemberAccessItem,
)


class PatchV2ListsListRequestData(pydantic.BaseModel):
    name: typing.Optional[str] = pydantic.Field(description="The human-readable name of the list.")
    api_slug: typing.Optional[str] = pydantic.Field(
        description="A unique, human-readable slug to access the list through API calls. Should be formatted in snake case."
    )
    workspace_access: typing.Optional[PatchV2ListsListRequestDataWorkspaceAccess] = pydantic.Field(
        description="The level of access granted to all members of the workspace for this list. Pass `null` to keep the list private and only grant access to specific workspace members."
    )
    workspace_member_access: typing.Optional[
        typing.List[PatchV2ListsListRequestDataWorkspaceMemberAccessItem]
    ] = pydantic.Field(
        description="The level of access granted to specific workspace members for this list. Pass an empty array to grant access to no workspace members."
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        
        json_encoders = {dt.datetime: serialize_datetime}
