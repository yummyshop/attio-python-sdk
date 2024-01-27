# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic as pydantic
import typing_extensions

from ....core.datetime_utils import serialize_datetime


class GetV2SelfResponseAud(pydantic.BaseModel):
    active: bool = pydantic.Field(description="Whether the token is currently active and usable.")
    scope: str = pydantic.Field(description="A space-separated list of scopes associated with this token")
    client_id: str = pydantic.Field(description="The app ID of the OAuth application that requested this token")
    token_type: typing_extensions.Literal["Bearer"]
    exp: typing.Optional[float] = pydantic.Field(
        description="The time at which this token will expire, if set, as a number of seconds since January 1 1970 UTC."
    )
    iat: float = pydantic.Field(
        description="The time at which this token was issued, as a number of seconds since January 1 1970 UTC."
    )
    sub: str = pydantic.Field(
        description="Since Bearer tokens grant Workspace-level permissions, this property contains the workspace_id."
    )
    aud: str = pydantic.Field(
        description="The intended audience for this token, for Bearer tokens this is the same as the client_id."
    )
    iss: typing_extensions.Literal["attio.com"]
    authorized_by_workspace_member_id: typing.Optional[str] = pydantic.Field(
        description="The ID of the workspace member who authorised this token initially, if known"
    )
    workspace_id: str = pydantic.Field(description="The ID of the workspace the token is scoped to.")
    workspace_name: str = pydantic.Field(description="The name of the workspace the token is scoped to.")
    workspace_slug: str = pydantic.Field(description="The slug of the workspace the token is scoped to.")
    workspace_logo_url: typing.Optional[str] = pydantic.Field(
        description="The logo URL of the workspace the token is scoped to."
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
