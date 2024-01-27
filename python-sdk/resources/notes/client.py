# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ...errors.not_found_error import NotFoundError
from .types.delete_v_2_notes_note_id_response import DeleteV2NotesNoteIdResponse
from .types.get_v_2_notes_note_id_response import GetV2NotesNoteIdResponse
from .types.get_v_2_notes_response import GetV2NotesResponse
from .types.post_v_2_notes_request_data import PostV2NotesRequestData
from .types.post_v_2_notes_response import PostV2NotesResponse

try:
    import pydantic as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class NotesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_notes(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        parent_object: typing.Optional[str] = None,
        parent_record_id: typing.Optional[str] = None,
    ) -> GetV2NotesResponse:
        """
        List notes for all records or for a specific record.

        Required scopes: `note:read`, `object_configuration:read`, `record_permission:read`.

        Parameters:
            - limit: typing.Optional[int].

            - offset: typing.Optional[int].

            - parent_object: typing.Optional[str].

            - parent_record_id: typing.Optional[str].
        ---
        from attio.client import attio_api

        client = attio_api(
            token="YOUR_TOKEN",
        )
        client.notes.list_notes(
            limit=1,
            offset=1,
            parent_object="people",
            parent_record_id="891dcbfc-9141-415d-9b2a-2238a6cc012d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v2/notes"),
            params=remove_none_from_dict(
                {"limit": limit, "offset": offset, "parent_object": parent_object, "parent_record_id": parent_record_id}
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetV2NotesResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_a_note(self, *, data: PostV2NotesRequestData) -> PostV2NotesResponse:
        """
        Creates a new note for a given record.

        At present, notes can only be created from plaintext without formatting.

        Required scopes: `note:read-write`, `object_configuration:read`, `record_permission:read`.

        Parameters:
            - data: PostV2NotesRequestData.
        ---
        from attio import PostV2NotesRequestData
        from attio.client import attio_api

        client = attio_api(token="YOUR_TOKEN", )
        client.notes.create_a_note(data=PostV2NotesRequestData(parent_object="people", parent_record_id="891dcbfc-9141-415d-9b2a-2238a6cc012d", title="Initial Prospecting Call Summary", format="plaintext", content="Introduction
        Date and time of the call
        Participants
        Purpose of the call
        Customer Background
        Company overview (industry, size, location)
        Key business challenges
        Current software solutions (if any) and pain points", created_at="2023-01-01T15:00:00.000000000Z", ), )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v2/notes"),
            json=jsonable_encoder({"data": data}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PostV2NotesResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_a_note(self, note_id: str) -> GetV2NotesNoteIdResponse:
        """
        Get a single note by ID.

        Required scopes: `note:read`, `object_configuration:read`, `record_permission:read`.

        Parameters:
            - note_id: str.
        ---
        from attio.client import attio_api

        client = attio_api(
            token="YOUR_TOKEN",
        )
        client.notes.get_a_note(
            note_id="ff3f3bd4-40f4-4f80-8187-cd02385af424",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/notes/{note_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetV2NotesNoteIdResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_a_note(self, note_id: str) -> DeleteV2NotesNoteIdResponse:
        """
        Delete a single note by ID.

        Required scopes: `note:read-write`.

        Parameters:
            - note_id: str.
        ---
        from attio.client import attio_api

        client = attio_api(
            token="YOUR_TOKEN",
        )
        client.notes.delete_a_note(
            note_id="ff3f3bd4-40f4-4f80-8187-cd02385af424",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/notes/{note_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DeleteV2NotesNoteIdResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncNotesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_notes(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        parent_object: typing.Optional[str] = None,
        parent_record_id: typing.Optional[str] = None,
    ) -> GetV2NotesResponse:
        """
        List notes for all records or for a specific record.

        Required scopes: `note:read`, `object_configuration:read`, `record_permission:read`.

        Parameters:
            - limit: typing.Optional[int].

            - offset: typing.Optional[int].

            - parent_object: typing.Optional[str].

            - parent_record_id: typing.Optional[str].
        ---
        from attio.client import Asyncattio_api

        client = Asyncattio_api(
            token="YOUR_TOKEN",
        )
        await client.notes.list_notes(
            limit=1,
            offset=1,
            parent_object="people",
            parent_record_id="891dcbfc-9141-415d-9b2a-2238a6cc012d",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v2/notes"),
            params=remove_none_from_dict(
                {"limit": limit, "offset": offset, "parent_object": parent_object, "parent_record_id": parent_record_id}
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetV2NotesResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_a_note(self, *, data: PostV2NotesRequestData) -> PostV2NotesResponse:
        """
        Creates a new note for a given record.

        At present, notes can only be created from plaintext without formatting.

        Required scopes: `note:read-write`, `object_configuration:read`, `record_permission:read`.

        Parameters:
            - data: PostV2NotesRequestData.
        ---
        from attio import PostV2NotesRequestData
        from attio.client import Asyncattio_api

        client = Asyncattio_api(token="YOUR_TOKEN", )
        await client.notes.create_a_note(data=PostV2NotesRequestData(parent_object="people", parent_record_id="891dcbfc-9141-415d-9b2a-2238a6cc012d", title="Initial Prospecting Call Summary", format="plaintext", content="Introduction
        Date and time of the call
        Participants
        Purpose of the call
        Customer Background
        Company overview (industry, size, location)
        Key business challenges
        Current software solutions (if any) and pain points", created_at="2023-01-01T15:00:00.000000000Z", ), )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v2/notes"),
            json=jsonable_encoder({"data": data}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PostV2NotesResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_a_note(self, note_id: str) -> GetV2NotesNoteIdResponse:
        """
        Get a single note by ID.

        Required scopes: `note:read`, `object_configuration:read`, `record_permission:read`.

        Parameters:
            - note_id: str.
        ---
        from attio.client import Asyncattio_api

        client = Asyncattio_api(
            token="YOUR_TOKEN",
        )
        await client.notes.get_a_note(
            note_id="ff3f3bd4-40f4-4f80-8187-cd02385af424",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/notes/{note_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetV2NotesNoteIdResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete_a_note(self, note_id: str) -> DeleteV2NotesNoteIdResponse:
        """
        Delete a single note by ID.

        Required scopes: `note:read-write`.

        Parameters:
            - note_id: str.
        ---
        from attio.client import Asyncattio_api

        client = Asyncattio_api(
            token="YOUR_TOKEN",
        )
        await client.notes.delete_a_note(
            note_id="ff3f3bd4-40f4-4f80-8187-cd02385af424",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/notes/{note_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DeleteV2NotesNoteIdResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
