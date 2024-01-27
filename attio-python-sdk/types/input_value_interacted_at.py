# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic as pydantic

from ..core.datetime_utils import serialize_datetime
from .input_value_interacted_at_interaction_type import InputValueInteractedAtInteractionType
from .input_value_interacted_at_owner_actor import InputValueInteractedAtOwnerActor


class InputValueInteractedAt(pydantic.BaseModel):
    interaction_type: InputValueInteractedAtInteractionType = pydantic.Field(
        description="The type of interaction e.g. calendar or email."
    )
    interacted_at: dt.datetime = pydantic.Field(description="When the interaction occurred.")
    owner_actor: InputValueInteractedAtOwnerActor = pydantic.Field(description="The actor that created this value.")

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