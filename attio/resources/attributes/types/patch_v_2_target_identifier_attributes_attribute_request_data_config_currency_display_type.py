# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PatchV2TargetIdentifierAttributesAttributeRequestDataConfigCurrencyDisplayType(str, enum.Enum):
    """
    How the currency should be displayed across the app. "code" will display the ISO currency code e.g. "USD", "name" will display the localized currency name e.g. "British pound", "narrowSymbol" will display "$1" instead of "US$1" and "symbol" will display a localized currency symbol such as "$".
    """

    CODE = "code"
    NAME = "name"
    NARROW_SYMBOL = "narrowSymbol"
    SYMBOL = "symbol"

    def visit(
        self,
        code: typing.Callable[[], T_Result],
        name: typing.Callable[[], T_Result],
        narrow_symbol: typing.Callable[[], T_Result],
        symbol: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PatchV2TargetIdentifierAttributesAttributeRequestDataConfigCurrencyDisplayType.CODE:
            return code()
        if self is PatchV2TargetIdentifierAttributesAttributeRequestDataConfigCurrencyDisplayType.NAME:
            return name()
        if self is PatchV2TargetIdentifierAttributesAttributeRequestDataConfigCurrencyDisplayType.NARROW_SYMBOL:
            return narrow_symbol()
        if self is PatchV2TargetIdentifierAttributesAttributeRequestDataConfigCurrencyDisplayType.SYMBOL:
            return symbol()
