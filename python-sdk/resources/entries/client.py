# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ...errors.bad_request_error import BadRequestError
from ...errors.not_found_error import NotFoundError
from .types.delete_v_2_lists_list_entries_entry_id_response import DeleteV2ListsListEntriesEntryIdResponse
from .types.get_v_2_lists_list_entries_entry_id_attributes_attribute_values_response import (
    GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponse,
)
from .types.get_v_2_lists_list_entries_entry_id_response import GetV2ListsListEntriesEntryIdResponse
from .types.patch_v_2_lists_list_entries_entry_id_request_data import PatchV2ListsListEntriesEntryIdRequestData
from .types.patch_v_2_lists_list_entries_entry_id_response import PatchV2ListsListEntriesEntryIdResponse
from .types.post_v_2_lists_list_entries_query_request_sorts_item import PostV2ListsListEntriesQueryRequestSortsItem
from .types.post_v_2_lists_list_entries_query_response import PostV2ListsListEntriesQueryResponse
from .types.post_v_2_lists_list_entries_request_data import PostV2ListsListEntriesRequestData
from .types.post_v_2_lists_list_entries_response import PostV2ListsListEntriesResponse
from .types.put_v_2_lists_list_entries_entry_id_request_data import PutV2ListsListEntriesEntryIdRequestData
from .types.put_v_2_lists_list_entries_entry_id_response import PutV2ListsListEntriesEntryIdResponse
from .types.put_v_2_lists_list_entries_request_data import PutV2ListsListEntriesRequestData
from .types.put_v_2_lists_list_entries_response import PutV2ListsListEntriesResponse

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class EntriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_entries(
        self,
        list: str,
        *,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        sorts: typing.Optional[typing.List[PostV2ListsListEntriesQueryRequestSortsItem]] = OMIT,
        limit: typing.Optional[float] = OMIT,
        offset: typing.Optional[float] = OMIT,
    ) -> PostV2ListsListEntriesQueryResponse:
        """
        Lists entries in a given list, with the option to filter and sort results.

        Required scopes: `list_entry:read`, `list_configuration:read`.

        Parameters:
            - list: str.

            - filter: typing.Optional[typing.Dict[str, typing.Any]]. An object used to filter results to a subset of results. See the [full guide to filtering and sorting here](/docs/filtering-and-sorting).

            - sorts: typing.Optional[typing.List[PostV2ListsListEntriesQueryRequestSortsItem]]. An object used to sort results. See the [full guide to filtering and sorting here](/docs/filtering-and-sorting).

            - limit: typing.Optional[float]. The maximum number of results to return. Defaults to 500. See the [full guide to pagination here](/docs/pagination).

            - offset: typing.Optional[float]. The number of results to skip over before returning. Defaults to 0. See the [full guide to pagination here](/docs/pagination).
        ---
        from attio.client import attio_api

        client = attio_api(
            token="YOUR_TOKEN",
        )
        client.entries.list_entries(
            list="33ebdbe9-e529-47c9-b894-0ba25e9c15c0",
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
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/lists/{list}/entries/query"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PostV2ListsListEntriesQueryResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_an_entry_add_record_to_list(
        self, list: str, *, data: PostV2ListsListEntriesRequestData
    ) -> PostV2ListsListEntriesResponse:
        """
        Adds a record to a list as a new list entry. This endpoint will throw on conflicts of unique attributes. Multiple list entries are allowed for the same parent record

        Required scopes: `list_entry:read-write`, `list_configuration:read`.

        Parameters:
            - list: str.

            - data: PostV2ListsListEntriesRequestData.
        ---
        from attio import PostV2ListsListEntriesRequestData
        from attio.client import attio_api

        client = attio_api(
            token="YOUR_TOKEN",
        )
        client.entries.create_an_entry_add_record_to_list(
            list="33ebdbe9-e529-47c9-b894-0ba25e9c15c0",
            data=PostV2ListsListEntriesRequestData(
                parent_record_id="891dcbfc-9141-415d-9b2a-2238a6cc012d",
                parent_object="people",
                entry_values={"string": []},
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/lists/{list}/entries"),
            json=jsonable_encoder({"data": data}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PostV2ListsListEntriesResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def assert_a_list_entry_by_parent(
        self, list: str, *, data: PutV2ListsListEntriesRequestData
    ) -> PutV2ListsListEntriesResponse:
        """
        Use this endpoint to create or update a list entry for a given parent record. If an entry with the specified parent record is found, that entry will be updated. If no such entry is found, a new entry will be created instead. If there are multiple entries with the same parent record, this endpoint with return the "MULTIPLE_MATCH_RESULTS" error. When writing to multi-select attributes, all values will be either created or deleted as necessary to match the list of values supplied in the request body.

        Required scopes: `list_entry:read-write`, `list_configuration:read`.

        Parameters:
            - list: str.

            - data: PutV2ListsListEntriesRequestData.
        ---
        from attio import PutV2ListsListEntriesRequestData
        from attio.client import attio_api

        client = attio_api(
            token="YOUR_TOKEN",
        )
        client.entries.assert_a_list_entry_by_parent(
            list="33ebdbe9-e529-47c9-b894-0ba25e9c15c0",
            data=PutV2ListsListEntriesRequestData(
                parent_record_id="891dcbfc-9141-415d-9b2a-2238a6cc012d",
                parent_object="people",
                entry_values={"string": []},
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/lists/{list}/entries"),
            json=jsonable_encoder({"data": data}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PutV2ListsListEntriesResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_a_list_entry(self, list: str, entry_id: str) -> GetV2ListsListEntriesEntryIdResponse:
        """
        Gets a single list entry by its `entry_id`.

        Required scopes: `list_entry:read`, `list_configuration:read`.

        Parameters:
            - list: str.

            - entry_id: str.
        ---
        from attio.client import attio_api

        client = attio_api(
            token="YOUR_TOKEN",
        )
        client.entries.get_a_list_entry(
            list="33ebdbe9-e529-47c9-b894-0ba25e9c15c0",
            entry_id="2e6e29ea-c4e0-4f44-842d-78a891f8c156",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/lists/{list}/entries/{entry_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetV2ListsListEntriesEntryIdResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update_a_list_entry_overwrite_multiselect_values(
        self, list: str, entry_id: str, *, data: PutV2ListsListEntriesEntryIdRequestData
    ) -> PutV2ListsListEntriesEntryIdResponse:
        """
        Use this endpoint to update list entries by `entry_id`. If the update payload includes multiselect attributes, the values supplied will overwrite/remove the list of values that already exist (if any). Use the `PATCH` endpoint to add multiselect attribute values without removing those value that already exist.

        Required scopes: `list_entry:read-write`, `list_configuration:read`.

        Parameters:
            - list: str.

            - entry_id: str.

            - data: PutV2ListsListEntriesEntryIdRequestData.
        ---
        from attio import PutV2ListsListEntriesEntryIdRequestData
        from attio.client import attio_api

        client = attio_api(
            token="YOUR_TOKEN",
        )
        client.entries.update_a_list_entry_overwrite_multiselect_values(
            list="33ebdbe9-e529-47c9-b894-0ba25e9c15c0",
            entry_id="2e6e29ea-c4e0-4f44-842d-78a891f8c156",
            data=PutV2ListsListEntriesEntryIdRequestData(
                entry_values={"string": []},
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/lists/{list}/entries/{entry_id}"),
            json=jsonable_encoder({"data": data}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PutV2ListsListEntriesEntryIdResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_a_list_entry(self, list: str, entry_id: str) -> DeleteV2ListsListEntriesEntryIdResponse:
        """
        Deletes a single list entry by its `entry_id`.

        Required scopes: `list_entry:read-write`, `list_configuration:read`.

        Parameters:
            - list: str.

            - entry_id: str.
        ---
        from attio.client import attio_api

        client = attio_api(
            token="YOUR_TOKEN",
        )
        client.entries.delete_a_list_entry(
            list="enterprise_sales",
            entry_id="2e6e29ea-c4e0-4f44-842d-78a891f8c156",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/lists/{list}/entries/{entry_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DeleteV2ListsListEntriesEntryIdResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update_a_list_entry_append_multiselect_values(
        self, list: str, entry_id: str, *, data: PatchV2ListsListEntriesEntryIdRequestData
    ) -> PatchV2ListsListEntriesEntryIdResponse:
        """
        Use this endpoint to update list entries by `entry_id`. If the update payload includes multiselect attributes, the values supplied will be created and prepended to the list of values that already exist (if any). Use the `PUT` endpoint to overwrite or remove multiselect attribute values.

        Required scopes: `list_entry:read-write`, `list_configuration:read`.

        Parameters:
            - list: str.

            - entry_id: str.

            - data: PatchV2ListsListEntriesEntryIdRequestData.
        ---
        from attio import PatchV2ListsListEntriesEntryIdRequestData
        from attio.client import attio_api

        client = attio_api(
            token="YOUR_TOKEN",
        )
        client.entries.update_a_list_entry_append_multiselect_values(
            list="33ebdbe9-e529-47c9-b894-0ba25e9c15c0",
            entry_id="2e6e29ea-c4e0-4f44-842d-78a891f8c156",
            data=PatchV2ListsListEntriesEntryIdRequestData(
                entry_values={"string": []},
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/lists/{list}/entries/{entry_id}"),
            json=jsonable_encoder({"data": data}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PatchV2ListsListEntriesEntryIdResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list_attribute_values_for_a_list_entry(
        self,
        list: str,
        entry_id: str,
        attribute: str,
        *,
        show_historic: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponse:
        """
        Gets all values for a given attribute on a list entry. If the attribute is historic, this endpoint has the ability to return all historic values using the `show_historic` query param.

        Required scopes: `list_entry:read`, `list_configuration:read`.

        Parameters:
            - list: str.

            - entry_id: str.

            - attribute: str.

            - show_historic: typing.Optional[bool].

            - limit: typing.Optional[int].

            - offset: typing.Optional[int].
        ---
        from attio.client import attio_api

        client = attio_api(
            token="YOUR_TOKEN",
        )
        client.entries.list_attribute_values_for_a_list_entry(
            list="enterprise_sales",
            entry_id="2e6e29ea-c4e0-4f44-842d-78a891f8c156",
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
                f"v2/lists/{list}/entries/{entry_id}/attributes/{attribute}/values",
            ),
            params=remove_none_from_dict({"show_historic": show_historic, "limit": limit, "offset": offset}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncEntriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_entries(
        self,
        list: str,
        *,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        sorts: typing.Optional[typing.List[PostV2ListsListEntriesQueryRequestSortsItem]] = OMIT,
        limit: typing.Optional[float] = OMIT,
        offset: typing.Optional[float] = OMIT,
    ) -> PostV2ListsListEntriesQueryResponse:
        """
        Lists entries in a given list, with the option to filter and sort results.

        Required scopes: `list_entry:read`, `list_configuration:read`.

        Parameters:
            - list: str.

            - filter: typing.Optional[typing.Dict[str, typing.Any]]. An object used to filter results to a subset of results. See the [full guide to filtering and sorting here](/docs/filtering-and-sorting).

            - sorts: typing.Optional[typing.List[PostV2ListsListEntriesQueryRequestSortsItem]]. An object used to sort results. See the [full guide to filtering and sorting here](/docs/filtering-and-sorting).

            - limit: typing.Optional[float]. The maximum number of results to return. Defaults to 500. See the [full guide to pagination here](/docs/pagination).

            - offset: typing.Optional[float]. The number of results to skip over before returning. Defaults to 0. See the [full guide to pagination here](/docs/pagination).
        ---
        from attio.client import Asyncattio_api

        client = Asyncattio_api(
            token="YOUR_TOKEN",
        )
        await client.entries.list_entries(
            list="33ebdbe9-e529-47c9-b894-0ba25e9c15c0",
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
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/lists/{list}/entries/query"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PostV2ListsListEntriesQueryResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_an_entry_add_record_to_list(
        self, list: str, *, data: PostV2ListsListEntriesRequestData
    ) -> PostV2ListsListEntriesResponse:
        """
        Adds a record to a list as a new list entry. This endpoint will throw on conflicts of unique attributes. Multiple list entries are allowed for the same parent record

        Required scopes: `list_entry:read-write`, `list_configuration:read`.

        Parameters:
            - list: str.

            - data: PostV2ListsListEntriesRequestData.
        ---
        from attio import PostV2ListsListEntriesRequestData
        from attio.client import Asyncattio_api

        client = Asyncattio_api(
            token="YOUR_TOKEN",
        )
        await client.entries.create_an_entry_add_record_to_list(
            list="33ebdbe9-e529-47c9-b894-0ba25e9c15c0",
            data=PostV2ListsListEntriesRequestData(
                parent_record_id="891dcbfc-9141-415d-9b2a-2238a6cc012d",
                parent_object="people",
                entry_values={"string": []},
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/lists/{list}/entries"),
            json=jsonable_encoder({"data": data}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PostV2ListsListEntriesResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def assert_a_list_entry_by_parent(
        self, list: str, *, data: PutV2ListsListEntriesRequestData
    ) -> PutV2ListsListEntriesResponse:
        """
        Use this endpoint to create or update a list entry for a given parent record. If an entry with the specified parent record is found, that entry will be updated. If no such entry is found, a new entry will be created instead. If there are multiple entries with the same parent record, this endpoint with return the "MULTIPLE_MATCH_RESULTS" error. When writing to multi-select attributes, all values will be either created or deleted as necessary to match the list of values supplied in the request body.

        Required scopes: `list_entry:read-write`, `list_configuration:read`.

        Parameters:
            - list: str.

            - data: PutV2ListsListEntriesRequestData.
        ---
        from attio import PutV2ListsListEntriesRequestData
        from attio.client import Asyncattio_api

        client = Asyncattio_api(
            token="YOUR_TOKEN",
        )
        await client.entries.assert_a_list_entry_by_parent(
            list="33ebdbe9-e529-47c9-b894-0ba25e9c15c0",
            data=PutV2ListsListEntriesRequestData(
                parent_record_id="891dcbfc-9141-415d-9b2a-2238a6cc012d",
                parent_object="people",
                entry_values={"string": []},
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/lists/{list}/entries"),
            json=jsonable_encoder({"data": data}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PutV2ListsListEntriesResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_a_list_entry(self, list: str, entry_id: str) -> GetV2ListsListEntriesEntryIdResponse:
        """
        Gets a single list entry by its `entry_id`.

        Required scopes: `list_entry:read`, `list_configuration:read`.

        Parameters:
            - list: str.

            - entry_id: str.
        ---
        from attio.client import Asyncattio_api

        client = Asyncattio_api(
            token="YOUR_TOKEN",
        )
        await client.entries.get_a_list_entry(
            list="33ebdbe9-e529-47c9-b894-0ba25e9c15c0",
            entry_id="2e6e29ea-c4e0-4f44-842d-78a891f8c156",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/lists/{list}/entries/{entry_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetV2ListsListEntriesEntryIdResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update_a_list_entry_overwrite_multiselect_values(
        self, list: str, entry_id: str, *, data: PutV2ListsListEntriesEntryIdRequestData
    ) -> PutV2ListsListEntriesEntryIdResponse:
        """
        Use this endpoint to update list entries by `entry_id`. If the update payload includes multiselect attributes, the values supplied will overwrite/remove the list of values that already exist (if any). Use the `PATCH` endpoint to add multiselect attribute values without removing those value that already exist.

        Required scopes: `list_entry:read-write`, `list_configuration:read`.

        Parameters:
            - list: str.

            - entry_id: str.

            - data: PutV2ListsListEntriesEntryIdRequestData.
        ---
        from attio import PutV2ListsListEntriesEntryIdRequestData
        from attio.client import Asyncattio_api

        client = Asyncattio_api(
            token="YOUR_TOKEN",
        )
        await client.entries.update_a_list_entry_overwrite_multiselect_values(
            list="33ebdbe9-e529-47c9-b894-0ba25e9c15c0",
            entry_id="2e6e29ea-c4e0-4f44-842d-78a891f8c156",
            data=PutV2ListsListEntriesEntryIdRequestData(
                entry_values={"string": []},
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/lists/{list}/entries/{entry_id}"),
            json=jsonable_encoder({"data": data}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PutV2ListsListEntriesEntryIdResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete_a_list_entry(self, list: str, entry_id: str) -> DeleteV2ListsListEntriesEntryIdResponse:
        """
        Deletes a single list entry by its `entry_id`.

        Required scopes: `list_entry:read-write`, `list_configuration:read`.

        Parameters:
            - list: str.

            - entry_id: str.
        ---
        from attio.client import Asyncattio_api

        client = Asyncattio_api(
            token="YOUR_TOKEN",
        )
        await client.entries.delete_a_list_entry(
            list="enterprise_sales",
            entry_id="2e6e29ea-c4e0-4f44-842d-78a891f8c156",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/lists/{list}/entries/{entry_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DeleteV2ListsListEntriesEntryIdResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update_a_list_entry_append_multiselect_values(
        self, list: str, entry_id: str, *, data: PatchV2ListsListEntriesEntryIdRequestData
    ) -> PatchV2ListsListEntriesEntryIdResponse:
        """
        Use this endpoint to update list entries by `entry_id`. If the update payload includes multiselect attributes, the values supplied will be created and prepended to the list of values that already exist (if any). Use the `PUT` endpoint to overwrite or remove multiselect attribute values.

        Required scopes: `list_entry:read-write`, `list_configuration:read`.

        Parameters:
            - list: str.

            - entry_id: str.

            - data: PatchV2ListsListEntriesEntryIdRequestData.
        ---
        from attio import PatchV2ListsListEntriesEntryIdRequestData
        from attio.client import Asyncattio_api

        client = Asyncattio_api(
            token="YOUR_TOKEN",
        )
        await client.entries.update_a_list_entry_append_multiselect_values(
            list="33ebdbe9-e529-47c9-b894-0ba25e9c15c0",
            entry_id="2e6e29ea-c4e0-4f44-842d-78a891f8c156",
            data=PatchV2ListsListEntriesEntryIdRequestData(
                entry_values={"string": []},
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/lists/{list}/entries/{entry_id}"),
            json=jsonable_encoder({"data": data}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PatchV2ListsListEntriesEntryIdResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list_attribute_values_for_a_list_entry(
        self,
        list: str,
        entry_id: str,
        attribute: str,
        *,
        show_historic: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponse:
        """
        Gets all values for a given attribute on a list entry. If the attribute is historic, this endpoint has the ability to return all historic values using the `show_historic` query param.

        Required scopes: `list_entry:read`, `list_configuration:read`.

        Parameters:
            - list: str.

            - entry_id: str.

            - attribute: str.

            - show_historic: typing.Optional[bool].

            - limit: typing.Optional[int].

            - offset: typing.Optional[int].
        ---
        from attio.client import Asyncattio_api

        client = Asyncattio_api(
            token="YOUR_TOKEN",
        )
        await client.entries.list_attribute_values_for_a_list_entry(
            list="enterprise_sales",
            entry_id="2e6e29ea-c4e0-4f44-842d-78a891f8c156",
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
                f"v2/lists/{list}/entries/{entry_id}/attributes/{attribute}/values",
            ),
            params=remove_none_from_dict({"show_historic": show_historic, "limit": limit, "offset": offset}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetV2ListsListEntriesEntryIdAttributesAttributeValuesResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
