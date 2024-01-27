# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PutV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemCurrencyCurrencyCode(str, enum.Enum):
    """
    The ISO4217 currency code representing the currency that the value is stored in.
    """

    EUR = "EUR"
    GBP = "GBP"
    USD = "USD"
    CAD = "CAD"
    AUD = "AUD"
    AED = "AED"
    INR = "INR"
    CHF = "CHF"
    JPY = "JPY"
    CNY = "CNY"
    PHP = "PHP"
    ILS = "ILS"
    SGD = "SGD"
    HKD = "HKD"
    MYR = "MYR"
    NTD = "NTD"
    NOK = "NOK"

    def visit(
        self,
        eur: typing.Callable[[], T_Result],
        gbp: typing.Callable[[], T_Result],
        usd: typing.Callable[[], T_Result],
        cad: typing.Callable[[], T_Result],
        aud: typing.Callable[[], T_Result],
        aed: typing.Callable[[], T_Result],
        inr: typing.Callable[[], T_Result],
        chf: typing.Callable[[], T_Result],
        jpy: typing.Callable[[], T_Result],
        cny: typing.Callable[[], T_Result],
        php: typing.Callable[[], T_Result],
        ils: typing.Callable[[], T_Result],
        sgd: typing.Callable[[], T_Result],
        hkd: typing.Callable[[], T_Result],
        myr: typing.Callable[[], T_Result],
        ntd: typing.Callable[[], T_Result],
        nok: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PutV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemCurrencyCurrencyCode.EUR:
            return eur()
        if self is PutV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemCurrencyCurrencyCode.GBP:
            return gbp()
        if self is PutV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemCurrencyCurrencyCode.USD:
            return usd()
        if self is PutV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemCurrencyCurrencyCode.CAD:
            return cad()
        if self is PutV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemCurrencyCurrencyCode.AUD:
            return aud()
        if self is PutV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemCurrencyCurrencyCode.AED:
            return aed()
        if self is PutV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemCurrencyCurrencyCode.INR:
            return inr()
        if self is PutV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemCurrencyCurrencyCode.CHF:
            return chf()
        if self is PutV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemCurrencyCurrencyCode.JPY:
            return jpy()
        if self is PutV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemCurrencyCurrencyCode.CNY:
            return cny()
        if self is PutV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemCurrencyCurrencyCode.PHP:
            return php()
        if self is PutV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemCurrencyCurrencyCode.ILS:
            return ils()
        if self is PutV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemCurrencyCurrencyCode.SGD:
            return sgd()
        if self is PutV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemCurrencyCurrencyCode.HKD:
            return hkd()
        if self is PutV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemCurrencyCurrencyCode.MYR:
            return myr()
        if self is PutV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemCurrencyCurrencyCode.NTD:
            return ntd()
        if self is PutV2ListsListEntriesEntryIdResponseDataEntryValuesValueItemCurrencyCurrencyCode.NOK:
            return nok()
