# This file was auto-generated by Fern from our API Definition.

import typing

from .input_value_slug_or_id_of_matching_attribute_slug_or_id_of_matching_attribute_item_country_code import (
    InputValueSlugOrIdOfMatchingAttributeSlugOrIdOfMatchingAttributeItemCountryCode,
)
from .input_value_slug_or_id_of_matching_attribute_slug_or_id_of_matching_attribute_item_domain import (
    InputValueSlugOrIdOfMatchingAttributeSlugOrIdOfMatchingAttributeItemDomain,
)
from .input_value_slug_or_id_of_matching_attribute_slug_or_id_of_matching_attribute_item_email_address import (
    InputValueSlugOrIdOfMatchingAttributeSlugOrIdOfMatchingAttributeItemEmailAddress,
)
from .input_value_slug_or_id_of_matching_attribute_slug_or_id_of_matching_attribute_item_four import (
    InputValueSlugOrIdOfMatchingAttributeSlugOrIdOfMatchingAttributeItemFour,
)
from .input_value_slug_or_id_of_matching_attribute_slug_or_id_of_matching_attribute_item_two import (
    InputValueSlugOrIdOfMatchingAttributeSlugOrIdOfMatchingAttributeItemTwo,
)

InputValueSlugOrIdOfMatchingAttributeSlugOrIdOfMatchingAttributeItem = typing.Union[
    InputValueSlugOrIdOfMatchingAttributeSlugOrIdOfMatchingAttributeItemDomain,
    InputValueSlugOrIdOfMatchingAttributeSlugOrIdOfMatchingAttributeItemEmailAddress,
    InputValueSlugOrIdOfMatchingAttributeSlugOrIdOfMatchingAttributeItemTwo,
    InputValueSlugOrIdOfMatchingAttributeSlugOrIdOfMatchingAttributeItemCountryCode,
    InputValueSlugOrIdOfMatchingAttributeSlugOrIdOfMatchingAttributeItemFour,
]
