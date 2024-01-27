# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.remove_none_from_dict import remove_none_from_dict
from ...errors.bad_request_error import BadRequestError
from ...errors.not_found_error import NotFoundError
from .types.delete_v_2_objects_object_records_record_id_response import DeleteV2ObjectsObjectRecordsRecordIdResponse
from .types.get_v_2_objects_object_records_record_id_attributes_attribute_values_response import (
    GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponse,
)
from .types.get_v_2_objects_object_records_record_id_entries_response import (
    GetV2ObjectsObjectRecordsRecordIdEntriesResponse,
)
from .types.get_v_2_objects_object_records_record_id_response import GetV2ObjectsObjectRecordsRecordIdResponse
from .types.patch_v_2_objects_object_records_record_id_request_data import (
    PatchV2ObjectsObjectRecordsRecordIdRequestData,
)
from .types.patch_v_2_objects_object_records_record_id_response import PatchV2ObjectsObjectRecordsRecordIdResponse
from .types.post_v_2_objects_object_records_query_request_sorts_item import (
    PostV2ObjectsObjectRecordsQueryRequestSortsItem,
)
from .types.post_v_2_objects_object_records_query_response import PostV2ObjectsObjectRecordsQueryResponse
from .types.post_v_2_objects_object_records_request_data import PostV2ObjectsObjectRecordsRequestData
from .types.post_v_2_objects_object_records_response import PostV2ObjectsObjectRecordsResponse
from .types.put_v_2_objects_object_records_request_data import PutV2ObjectsObjectRecordsRequestData
from .types.put_v_2_objects_object_records_response import PutV2ObjectsObjectRecordsResponse
import json

try:
    import pydantic as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RecordsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_records(
        self,
        object: str,
        *,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        sorts: typing.Optional[typing.List[PostV2ObjectsObjectRecordsQueryRequestSortsItem]] = OMIT,
        limit: typing.Optional[float] = OMIT,
        offset: typing.Optional[float] = OMIT,
    ) -> PostV2ObjectsObjectRecordsQueryResponse:
        """
        Lists people, company or other records, with the option to filter and sort results.

        Required scopes: `record_permission:read`, `object_configuration:read`.

        Parameters:
            - object: str.

            - filter: typing.Optional[typing.Dict[str, typing.Any]]. An object used to filter results to a subset of results. See the [full guide to filtering and sorting here](/docs/filtering-and-sorting).

            - sorts: typing.Optional[typing.List[PostV2ObjectsObjectRecordsQueryRequestSortsItem]]. An object used to sort results. See the [full guide to filtering and sorting here](/docs/filtering-and-sorting).

            - limit: typing.Optional[float]. The maximum number of results to return. Defaults to 500. See the [full guide to pagination here](/docs/pagination).

            - offset: typing.Optional[float]. The number of results to skip over before returning. Defaults to 0. See the [full guide to pagination here](/docs/pagination).
        ---
        from attio.client import AttioClient

        client = AttioClient(
            token="YOUR_TOKEN",
        )
        client.records.list_records(
            object="people",
            sorts=[],
            limit=500.0,
            offset=0.0,
        )
        """
        _request: typing.Dict[str, typing.Any] = {}
        if filter is not OMIT:
            _request["filter"] = filter
        if sorts is not OMIT:
            _request["sorts"] = sorts
        if limit is not OMIT:
            _request["limit"] = limit
        if offset is not OMIT:
            _request["offset"] = offset
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/objects/{object}/records/query"),
            json=_request,
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PostV2ObjectsObjectRecordsQueryResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_a_record(
        self, object: str, *, data: PostV2ObjectsObjectRecordsRequestData
    ) -> PostV2ObjectsObjectRecordsResponse:
        """
        Creates a new person, company or other record. This endpoint will throw on conflicts of unique attributes. If you would prefer to update records on conflicts, please use the [Assert record endpoint](/reference/put_v2-objects-object-records) instead.

        Required scopes: `record_permission:read-write`, `object_configuration:read`.

        Parameters:
            - object: str.

            - data: PostV2ObjectsObjectRecordsRequestData.
        ---
        from attio import PostV2ObjectsObjectRecordsRequestData
        from attio.client import AttioClient

        client = AttioClient(
            token="YOUR_TOKEN",
        )
        client.records.create_a_record(
            object="people",
            data=PostV2ObjectsObjectRecordsRequestData(
                values={"string": []},
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/objects/{object}/records"),
            json={"data": data.model_dump_json()},
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PostV2ObjectsObjectRecordsResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def assert_a_record(
        self, object: str, *, matching_attribute: str, data: PutV2ObjectsObjectRecordsRequestData
    ) -> PutV2ObjectsObjectRecordsResponse:
        """
        Use this endpoint to create or update people, companies and other records. A matching attribute is used to search for existing records. If a record is found with the same value for the matching attribute, that record will be updated. If no record with the same value for the matching attribute is found, a new record will be created instead. If you would like to avoid matching, please use the [Create record endpoint](/reference/post_v2-objects-object-records).

        If the matching attribute is a multiselect attribute, new values will be added and existing values will not be deleted. For any other multiselect attribute, all values will be either created or deleted as necessary to match the list of supplied values.

        Required scopes: `record_permission:read-write`, `object_configuration:read`.

        Parameters:
            - object: str.

            - matching_attribute: str.

            - data: PutV2ObjectsObjectRecordsRequestData.
        ---
        from attio import PutV2ObjectsObjectRecordsRequestData
        from attio.client import AttioClient

        client = AttioClient(
            token="YOUR_TOKEN",
        )
        client.records.assert_a_record(
            object="people",
            matching_attribute="41252299-f8c7-4b5e-99c9-4ff8321d2f96",
            data=PutV2ObjectsObjectRecordsRequestData(
                values={"string": []},
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/objects/{object}/records"),
            params=remove_none_from_dict({"matching_attribute": matching_attribute}),
            json={"data": data.model_dump_json()},
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PutV2ObjectsObjectRecordsResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_a_record(self, object: str, record_id: str) -> GetV2ObjectsObjectRecordsRecordIdResponse:
        """
        Gets a single person, company or other record by its `record_id`.

        Required scopes: `record_permission:read`, `object_configuration:read`.

        Parameters:
            - object: str.

            - record_id: str.
        ---
        from attio.client import AttioClient

        client = AttioClient(
            token="YOUR_TOKEN",
        )
        client.records.get_a_record(
            object="people",
            record_id="891dcbfc-9141-415d-9b2a-2238a6cc012d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/objects/{object}/records/{record_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetV2ObjectsObjectRecordsRecordIdResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_a_record(self, object: str, record_id: str) -> DeleteV2ObjectsObjectRecordsRecordIdResponse:
        """
        Deletes a single record (e.g. a company or person) by ID.

        Required scopes: `object_configuration:read`, `record_permission:read-write`.

        Parameters:
            - object: str.

            - record_id: str.
        ---
        from attio.client import AttioClient

        client = AttioClient(
            token="YOUR_TOKEN",
        )
        client.records.delete_a_record(
            object="people",
            record_id="891dcbfc-9141-415d-9b2a-2238a6cc012d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/objects/{object}/records/{record_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DeleteV2ObjectsObjectRecordsRecordIdResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update_a_record(
        self, object: str, record_id: str, *, data: PatchV2ObjectsObjectRecordsRecordIdRequestData
    ) -> PatchV2ObjectsObjectRecordsRecordIdResponse:
        """
        Use this endpoint to update people, companies and other records by `record_id`. If the update payload includes multiselect attributes, the values supplied will be created and prepended to the list of values that already exist (if any). Use the [Assert record endpoint](/reference/put_v2-objects-object-records) to overwrite or remove multiselect attribute values.

        Required scopes: `record_permission:read-write`, `object_configuration:read`.

        Parameters:
            - object: str.

            - record_id: str.

            - data: PatchV2ObjectsObjectRecordsRecordIdRequestData.
        ---
        from attio import PatchV2ObjectsObjectRecordsRecordIdRequestData
        from attio.client import AttioClient

        client = AttioClient(
            token="YOUR_TOKEN",
        )
        client.records.update_a_record(
            object="people",
            record_id="891dcbfc-9141-415d-9b2a-2238a6cc012d",
            data=PatchV2ObjectsObjectRecordsRecordIdRequestData(
                values={"string": []},
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/objects/{object}/records/{record_id}"),
            json={"data": data.model_dump_json()},
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PatchV2ObjectsObjectRecordsRecordIdResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list_record_attribute_values(
        self,
        object: str,
        record_id: str,
        attribute: str,
        *,
        show_historic: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponse:
        """
        Gets all values for a given attribute on a record. If the attribute is historic, this endpoint has the ability to return all historic values using the `show_historic` query param.

        Required scopes: `record_permission:read`, `object_configuration:read`.

        Parameters:
            - object: str.

            - record_id: str.

            - attribute: str.

            - show_historic: typing.Optional[bool].

            - limit: typing.Optional[int].

            - offset: typing.Optional[int].
        ---
        from attio.client import AttioClient

        client = AttioClient(
            token="YOUR_TOKEN",
        )
        client.records.list_record_attribute_values(
            object="people",
            record_id="891dcbfc-9141-415d-9b2a-2238a6cc012d",
            attribute="41252299-f8c7-4b5e-99c9-4ff8321d2f96",
            show_historic=True,
            limit=1,
            offset=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"v2/objects/{object}/records/{record_id}/attributes/{attribute}/values",
            ),
            params=remove_none_from_dict({"show_historic": show_historic, "limit": limit, "offset": offset}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list_record_entries(
        self, object: str, record_id: str, *, limit: typing.Optional[int] = None, offset: typing.Optional[int] = None
    ) -> GetV2ObjectsObjectRecordsRecordIdEntriesResponse:
        """
        List all entries, across all lists, for which this record is the parent.

        Required scopes: `record_permission:read`, `object_configuration:read`, `list_entry:read`.

        Parameters:
            - object: str.

            - record_id: str.

            - limit: typing.Optional[int].

            - offset: typing.Optional[int].
        ---
        from attio.client import AttioClient

        client = AttioClient(
            token="YOUR_TOKEN",
        )
        client.records.list_record_entries(
            object="people",
            record_id="891dcbfc-9141-415d-9b2a-2238a6cc012d",
            limit=1,
            offset=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"v2/objects/{object}/records/{record_id}/entries"
            ),
            params=remove_none_from_dict({"limit": limit, "offset": offset}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetV2ObjectsObjectRecordsRecordIdEntriesResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncRecordsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_records(
        self,
        object: str,
        *,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        sorts: typing.Optional[typing.List[PostV2ObjectsObjectRecordsQueryRequestSortsItem]] = OMIT,
        limit: typing.Optional[float] = OMIT,
        offset: typing.Optional[float] = OMIT,
    ) -> PostV2ObjectsObjectRecordsQueryResponse:
        """
        Lists people, company or other records, with the option to filter and sort results.

        Required scopes: `record_permission:read`, `object_configuration:read`.

        Parameters:
            - object: str.

            - filter: typing.Optional[typing.Dict[str, typing.Any]]. An object used to filter results to a subset of results. See the [full guide to filtering and sorting here](/docs/filtering-and-sorting).

            - sorts: typing.Optional[typing.List[PostV2ObjectsObjectRecordsQueryRequestSortsItem]]. An object used to sort results. See the [full guide to filtering and sorting here](/docs/filtering-and-sorting).

            - limit: typing.Optional[float]. The maximum number of results to return. Defaults to 500. See the [full guide to pagination here](/docs/pagination).

            - offset: typing.Optional[float]. The number of results to skip over before returning. Defaults to 0. See the [full guide to pagination here](/docs/pagination).
        ---
        from attio.client import AsyncAttioClient

        client = AsyncAttioClient(
            token="YOUR_TOKEN",
        )
        await client.records.list_records(
            object="people",
            sorts=[],
            limit=500.0,
            offset=0.0,
        )
        """
        _request: typing.Dict[str, typing.Any] = {}
        if filter is not OMIT:
            _request["filter"] = filter
        if sorts is not OMIT:
            _request["sorts"] = sorts
        if limit is not OMIT:
            _request["limit"] = limit
        if offset is not OMIT:
            _request["offset"] = offset
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/objects/{object}/records/query"),
            json=_request,
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PostV2ObjectsObjectRecordsQueryResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_a_record(
        self, object: str, *, data: PostV2ObjectsObjectRecordsRequestData
    ) -> PostV2ObjectsObjectRecordsResponse:
        """
        Creates a new person, company or other record. This endpoint will throw on conflicts of unique attributes. If you would prefer to update records on conflicts, please use the [Assert record endpoint](/reference/put_v2-objects-object-records) instead.

        Required scopes: `record_permission:read-write`, `object_configuration:read`.

        Parameters:
            - object: str.

            - data: PostV2ObjectsObjectRecordsRequestData.
        ---
        from attio import PostV2ObjectsObjectRecordsRequestData
        from attio.client import AsyncAttioClient

        client = AsyncAttioClient(
            token="YOUR_TOKEN",
        )
        await client.records.create_a_record(
            object="people",
            data=PostV2ObjectsObjectRecordsRequestData(
                values={"string": []},
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/objects/{object}/records"),
            json={"data": data.model_dump_json()},
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PostV2ObjectsObjectRecordsResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def assert_a_record(
        self, object: str, *, matching_attribute: str, data: PutV2ObjectsObjectRecordsRequestData
    ) -> PutV2ObjectsObjectRecordsResponse:
        """
        Use this endpoint to create or update people, companies and other records. A matching attribute is used to search for existing records. If a record is found with the same value for the matching attribute, that record will be updated. If no record with the same value for the matching attribute is found, a new record will be created instead. If you would like to avoid matching, please use the [Create record endpoint](/reference/post_v2-objects-object-records).

        If the matching attribute is a multiselect attribute, new values will be added and existing values will not be deleted. For any other multiselect attribute, all values will be either created or deleted as necessary to match the list of supplied values.

        Required scopes: `record_permission:read-write`, `object_configuration:read`.

        Parameters:
            - object: str.

            - matching_attribute: str.

            - data: PutV2ObjectsObjectRecordsRequestData.
        ---
        from attio import PutV2ObjectsObjectRecordsRequestData
        from attio.client import AsyncAttioClient

        client = AsyncAttioClient(
            token="YOUR_TOKEN",
        )
        await client.records.assert_a_record(
            object="people",
            matching_attribute="41252299-f8c7-4b5e-99c9-4ff8321d2f96",
            data=PutV2ObjectsObjectRecordsRequestData(
                values={"string": []},
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/objects/{object}/records"),
            params=remove_none_from_dict({"matching_attribute": matching_attribute}),
            json={"data": data.model_dump_json()},
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PutV2ObjectsObjectRecordsResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_a_record(self, object: str, record_id: str) -> GetV2ObjectsObjectRecordsRecordIdResponse:
        """
        Gets a single person, company or other record by its `record_id`.

        Required scopes: `record_permission:read`, `object_configuration:read`.

        Parameters:
            - object: str.

            - record_id: str.
        ---
        from attio.client import AsyncAttioClient

        client = AsyncAttioClient(
            token="YOUR_TOKEN",
        )
        await client.records.get_a_record(
            object="people",
            record_id="891dcbfc-9141-415d-9b2a-2238a6cc012d",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/objects/{object}/records/{record_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetV2ObjectsObjectRecordsRecordIdResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete_a_record(self, object: str, record_id: str) -> DeleteV2ObjectsObjectRecordsRecordIdResponse:
        """
        Deletes a single record (e.g. a company or person) by ID.

        Required scopes: `object_configuration:read`, `record_permission:read-write`.

        Parameters:
            - object: str.

            - record_id: str.
        ---
        from attio.client import AsyncAttioClient

        client = AsyncAttioClient(
            token="YOUR_TOKEN",
        )
        await client.records.delete_a_record(
            object="people",
            record_id="891dcbfc-9141-415d-9b2a-2238a6cc012d",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/objects/{object}/records/{record_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DeleteV2ObjectsObjectRecordsRecordIdResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update_a_record(
        self, object: str, record_id: str, *, data: PatchV2ObjectsObjectRecordsRecordIdRequestData
    ) -> PatchV2ObjectsObjectRecordsRecordIdResponse:
        """
        Use this endpoint to update people, companies and other records by `record_id`. If the update payload includes multiselect attributes, the values supplied will be created and prepended to the list of values that already exist (if any). Use the [Assert record endpoint](/reference/put_v2-objects-object-records) to overwrite or remove multiselect attribute values.

        Required scopes: `record_permission:read-write`, `object_configuration:read`.

        Parameters:
            - object: str.

            - record_id: str.

            - data: PatchV2ObjectsObjectRecordsRecordIdRequestData.
        ---
        from attio import PatchV2ObjectsObjectRecordsRecordIdRequestData
        from attio.client import AsyncAttioClient

        client = AsyncAttioClient(
            token="YOUR_TOKEN",
        )
        await client.records.update_a_record(
            object="people",
            record_id="891dcbfc-9141-415d-9b2a-2238a6cc012d",
            data=PatchV2ObjectsObjectRecordsRecordIdRequestData(
                values={"string": []},
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/objects/{object}/records/{record_id}"),
            json={"data": data.model_dump_json()},
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PatchV2ObjectsObjectRecordsRecordIdResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list_record_attribute_values(
        self,
        object: str,
        record_id: str,
        attribute: str,
        *,
        show_historic: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponse:
        """
        Gets all values for a given attribute on a record. If the attribute is historic, this endpoint has the ability to return all historic values using the `show_historic` query param.

        Required scopes: `record_permission:read`, `object_configuration:read`.

        Parameters:
            - object: str.

            - record_id: str.

            - attribute: str.

            - show_historic: typing.Optional[bool].

            - limit: typing.Optional[int].

            - offset: typing.Optional[int].
        ---
        from attio.client import AsyncAttioClient

        client = AsyncAttioClient(
            token="YOUR_TOKEN",
        )
        await client.records.list_record_attribute_values(
            object="people",
            record_id="891dcbfc-9141-415d-9b2a-2238a6cc012d",
            attribute="41252299-f8c7-4b5e-99c9-4ff8321d2f96",
            show_historic=True,
            limit=1,
            offset=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"v2/objects/{object}/records/{record_id}/attributes/{attribute}/values",
            ),
            params=remove_none_from_dict({"show_historic": show_historic, "limit": limit, "offset": offset}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetV2ObjectsObjectRecordsRecordIdAttributesAttributeValuesResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list_record_entries(
        self, object: str, record_id: str, *, limit: typing.Optional[int] = None, offset: typing.Optional[int] = None
    ) -> GetV2ObjectsObjectRecordsRecordIdEntriesResponse:
        """
        List all entries, across all lists, for which this record is the parent.

        Required scopes: `record_permission:read`, `object_configuration:read`, `list_entry:read`.

        Parameters:
            - object: str.

            - record_id: str.

            - limit: typing.Optional[int].

            - offset: typing.Optional[int].
        ---
        from attio.client import AsyncAttioClient

        client = AsyncAttioClient(
            token="YOUR_TOKEN",
        )
        await client.records.list_record_entries(
            object="people",
            record_id="891dcbfc-9141-415d-9b2a-2238a6cc012d",
            limit=1,
            offset=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"v2/objects/{object}/records/{record_id}/entries"
            ),
            params=remove_none_from_dict({"limit": limit, "offset": offset}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetV2ObjectsObjectRecordsRecordIdEntriesResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
