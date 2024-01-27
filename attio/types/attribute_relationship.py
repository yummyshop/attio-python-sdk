# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic as pydantic

from ..core.datetime_utils import serialize_datetime
from .attribute_relationship_id import AttributeRelationshipId


class AttributeRelationship(pydantic.BaseModel):
    """
    If this attribute is related to another attribute, this is an object that includes an `id` property that identifies the other attribute. `null` means no relationship exists. See [the help center](https://attio.com/help/reference/managing-your-data/attributes#relationship-attributes) for more details about relationship attributes.
    """

    id: AttributeRelationshipId

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        
        json_encoders = {dt.datetime: serialize_datetime}
