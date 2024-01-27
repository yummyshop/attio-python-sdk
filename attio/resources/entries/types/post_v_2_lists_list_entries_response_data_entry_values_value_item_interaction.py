# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic as pydantic

from ....core.datetime_utils import serialize_datetime
from .post_v_2_lists_list_entries_response_data_entry_values_value_item_interaction_created_by_actor import (
    PostV2ListsListEntriesResponseDataEntryValuesValueItemInteractionCreatedByActor,
)
from .post_v_2_lists_list_entries_response_data_entry_values_value_item_interaction_interaction_type import (
    PostV2ListsListEntriesResponseDataEntryValuesValueItemInteractionInteractionType,
)
from .post_v_2_lists_list_entries_response_data_entry_values_value_item_interaction_owner_actor import (
    PostV2ListsListEntriesResponseDataEntryValuesValueItemInteractionOwnerActor,
)


class PostV2ListsListEntriesResponseDataEntryValuesValueItemInteraction(pydantic.BaseModel):
    active_from: dt.datetime = pydantic.Field(
        description='The point in time at which this value was made "active". `active_from` can be considered roughly analogous to `created_at`.'
    )
    active_until: typing.Optional[dt.datetime] = pydantic.Field(
        description="The point in time at which this value was deactivated. If `null`, the value is active."
    )
    created_by_actor: PostV2ListsListEntriesResponseDataEntryValuesValueItemInteractionCreatedByActor = pydantic.Field(
        description="The actor that created this value."
    )
    interaction_type: PostV2ListsListEntriesResponseDataEntryValuesValueItemInteractionInteractionType = pydantic.Field(
        description="The type of interaction e.g. calendar or email."
    )
    interacted_at: dt.datetime = pydantic.Field(description="When the interaction occurred.")
    owner_actor: PostV2ListsListEntriesResponseDataEntryValuesValueItemInteractionOwnerActor = pydantic.Field(
        description="The actor that created this value."
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
