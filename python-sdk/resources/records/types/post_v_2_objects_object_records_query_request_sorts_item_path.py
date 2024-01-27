# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic.v1 as pydantic

from ....core.datetime_utils import serialize_datetime
from .post_v_2_objects_object_records_query_request_sorts_item_path_direction import (
    PostV2ObjectsObjectRecordsQueryRequestSortsItemPathDirection,
)


class PostV2ObjectsObjectRecordsQueryRequestSortsItemPath(pydantic.BaseModel):
    """
    Sort by path
    """

    direction: PostV2ObjectsObjectRecordsQueryRequestSortsItemPathDirection = pydantic.Field(
        description="The direction to sort the results by."
    )
    path: typing.List[typing.List[str]] = pydantic.Field(
        description="You may use the `path` property to traverse record reference attributes and parent records on list entries. `path` accepts an array of tuples where the first element of each tuple is the slug or ID of a list/object, and the second element is the slug or ID of an attribute on that list/object. The first element of the first tuple must correspond to the list or object that you are querying. For example, if you wanted to sort by the name of the parent record (a company) on a list with the slug \"sales\", you would pass the value `[['sales', 'parent_record'], ['companies', 'name']]`."
    )
    field: typing.Optional[str] = pydantic.Field(
        description='Which field on the value to sort by e.g. "last_name" on a name value.'
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
