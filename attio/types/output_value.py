# This file was auto-generated by Fern from our API Definition.

import typing

from .output_value_attribute_type import OutputValueAttributeType
from .output_value_currency_code import OutputValueCurrencyCode
from .output_value_domain import OutputValueDomain
from .output_value_email_address import OutputValueEmailAddress
from .output_value_fifteen import OutputValueFifteen
from .output_value_first_name import OutputValueFirstName
from .output_value_fourteen import OutputValueFourteen
from .output_value_interacted_at import OutputValueInteractedAt
from .output_value_latitude import OutputValueLatitude
from .output_value_nine import OutputValueNine
from .output_value_one import OutputValueOne
from .output_value_original_phone_number import OutputValueOriginalPhoneNumber
from .output_value_referenced_actor_id import OutputValueReferencedActorId
from .output_value_seventeen import OutputValueSeventeen
from .output_value_sixteen import OutputValueSixteen
from .output_value_target_object import OutputValueTargetObject
from .output_value_thirteen import OutputValueThirteen
from .output_value_three import OutputValueThree
from .output_value_twelve import OutputValueTwelve

OutputValue = typing.Union[
    OutputValueReferencedActorId,
    OutputValueOne,
    OutputValueCurrencyCode,
    OutputValueThree,
    OutputValueDomain,
    OutputValueEmailAddress,
    OutputValueTargetObject,
    OutputValueInteractedAt,
    OutputValueLatitude,
    OutputValueNine,
    OutputValueFirstName,
    OutputValueOriginalPhoneNumber,
    OutputValueTwelve,
    OutputValueThirteen,
    OutputValueFourteen,
    OutputValueFifteen,
    OutputValueSixteen,
    OutputValueSeventeen,
    OutputValueAttributeType,
]
