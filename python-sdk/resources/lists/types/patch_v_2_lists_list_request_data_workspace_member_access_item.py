# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic as pydantic

from ....core.datetime_utils import serialize_datetime
from .patch_v_2_lists_list_request_data_workspace_member_access_item_level import (
    PatchV2ListsListRequestDataWorkspaceMemberAccessItemLevel,
)


class PatchV2ListsListRequestDataWorkspaceMemberAccessItem(pydantic.BaseModel):
    workspace_member_id: str = pydantic.Field(description="A UUID to identify the workspace member to grant access to.")
    level: PatchV2ListsListRequestDataWorkspaceMemberAccessItemLevel = pydantic.Field(
        description="The level of access to the list."
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
