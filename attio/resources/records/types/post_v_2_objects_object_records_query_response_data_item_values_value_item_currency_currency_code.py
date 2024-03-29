# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemCurrencyCurrencyCode(str, enum.Enum):
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
        if self is PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemCurrencyCurrencyCode.EUR:
            return eur()
        if self is PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemCurrencyCurrencyCode.GBP:
            return gbp()
        if self is PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemCurrencyCurrencyCode.USD:
            return usd()
        if self is PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemCurrencyCurrencyCode.CAD:
            return cad()
        if self is PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemCurrencyCurrencyCode.AUD:
            return aud()
        if self is PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemCurrencyCurrencyCode.AED:
            return aed()
        if self is PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemCurrencyCurrencyCode.INR:
            return inr()
        if self is PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemCurrencyCurrencyCode.CHF:
            return chf()
        if self is PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemCurrencyCurrencyCode.JPY:
            return jpy()
        if self is PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemCurrencyCurrencyCode.CNY:
            return cny()
        if self is PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemCurrencyCurrencyCode.PHP:
            return php()
        if self is PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemCurrencyCurrencyCode.ILS:
            return ils()
        if self is PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemCurrencyCurrencyCode.SGD:
            return sgd()
        if self is PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemCurrencyCurrencyCode.HKD:
            return hkd()
        if self is PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemCurrencyCurrencyCode.MYR:
            return myr()
        if self is PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemCurrencyCurrencyCode.NTD:
            return ntd()
        if self is PostV2ObjectsObjectRecordsQueryResponseDataItemValuesValueItemCurrencyCurrencyCode.NOK:
            return nok()
