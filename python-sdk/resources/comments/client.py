# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...errors.bad_request_error import BadRequestError
from ...errors.not_found_error import NotFoundError
from .types.delete_v_2_comments_comment_id_response import DeleteV2CommentsCommentIdResponse
from .types.get_v_2_comments_comment_id_response import GetV2CommentsCommentIdResponse
from .types.post_v_2_comments_request_data import PostV2CommentsRequestData
from .types.post_v_2_comments_response import PostV2CommentsResponse

try:
    import pydantic as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class CommentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_a_comment(self, *, data: PostV2CommentsRequestData) -> PostV2CommentsResponse:
        """
        Creates a new comment related to an existing thread, record or entry.

        To create comments on records, you will need the `object_configuration:read` and `record_permission:read` scopes.

        To create comments on list entries, you will need the `list_configuration:read` and `list_entry:read` scopes.

        Required scopes: `comment:read-write`.

        Parameters:
            - data: PostV2CommentsRequestData.
        ---
        from attio.client import attio_api

        client = attio_api(
            token="YOUR_TOKEN",
        )
        client.comments.create_a_comment()
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v2/comments"),
            json=jsonable_encoder({"data": data}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PostV2CommentsResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_a_comment(self, comment_id: str) -> GetV2CommentsCommentIdResponse:
        """
        Get a single comment by ID.

        To view comments on records, you will need the `object_configuration:read` and `record_permission:read` scopes.

        To view comments on list entries, you will need the `list_configuration:read` and `list_entry:read` scopes.

        Required scopes: `comment:read`.

        Parameters:
            - comment_id: str.
        ---
        from attio.client import attio_api

        client = attio_api(
            token="YOUR_TOKEN",
        )
        client.comments.get_a_comment(
            comment_id="aa1dc1d9-93ac-4c6c-987e-16b6eea9aab2",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/comments/{comment_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetV2CommentsCommentIdResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_a_comment(self, comment_id: str) -> DeleteV2CommentsCommentIdResponse:
        """
        Deletes a comment by ID. If deleting a comment at the head of a thread, all messages in the thread are also deleted.

        Required scopes: `comment:read-write`.

        Parameters:
            - comment_id: str.
        ---
        from attio.client import attio_api

        client = attio_api(
            token="YOUR_TOKEN",
        )
        client.comments.delete_a_comment(
            comment_id="aa1dc1d9-93ac-4c6c-987e-16b6eea9aab2",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/comments/{comment_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DeleteV2CommentsCommentIdResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncCommentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_a_comment(self, *, data: PostV2CommentsRequestData) -> PostV2CommentsResponse:
        """
        Creates a new comment related to an existing thread, record or entry.

        To create comments on records, you will need the `object_configuration:read` and `record_permission:read` scopes.

        To create comments on list entries, you will need the `list_configuration:read` and `list_entry:read` scopes.

        Required scopes: `comment:read-write`.

        Parameters:
            - data: PostV2CommentsRequestData.
        ---
        from attio.client import Asyncattio_api

        client = Asyncattio_api(
            token="YOUR_TOKEN",
        )
        await client.comments.create_a_comment()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v2/comments"),
            json=jsonable_encoder({"data": data}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PostV2CommentsResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_a_comment(self, comment_id: str) -> GetV2CommentsCommentIdResponse:
        """
        Get a single comment by ID.

        To view comments on records, you will need the `object_configuration:read` and `record_permission:read` scopes.

        To view comments on list entries, you will need the `list_configuration:read` and `list_entry:read` scopes.

        Required scopes: `comment:read`.

        Parameters:
            - comment_id: str.
        ---
        from attio.client import Asyncattio_api

        client = Asyncattio_api(
            token="YOUR_TOKEN",
        )
        await client.comments.get_a_comment(
            comment_id="aa1dc1d9-93ac-4c6c-987e-16b6eea9aab2",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/comments/{comment_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetV2CommentsCommentIdResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete_a_comment(self, comment_id: str) -> DeleteV2CommentsCommentIdResponse:
        """
        Deletes a comment by ID. If deleting a comment at the head of a thread, all messages in the thread are also deleted.

        Required scopes: `comment:read-write`.

        Parameters:
            - comment_id: str.
        ---
        from attio.client import Asyncattio_api

        client = Asyncattio_api(
            token="YOUR_TOKEN",
        )
        await client.comments.delete_a_comment(
            comment_id="aa1dc1d9-93ac-4c6c-987e-16b6eea9aab2",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/comments/{comment_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DeleteV2CommentsCommentIdResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
