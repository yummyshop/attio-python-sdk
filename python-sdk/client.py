# This file was auto-generated by Fern from our API Definition.

import typing

import httpx

from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .environment import attio_apiEnvironment
from .resources.attributes.client import AsyncAttributesClient, AttributesClient
from .resources.comments.client import AsyncCommentsClient, CommentsClient
from .resources.entries.client import AsyncEntriesClient, EntriesClient
from .resources.lists.client import AsyncListsClient, ListsClient
from .resources.meta.client import AsyncMetaClient, MetaClient
from .resources.notes.client import AsyncNotesClient, NotesClient
from .resources.objects.client import AsyncObjectsClient, ObjectsClient
from .resources.records.client import AsyncRecordsClient, RecordsClient
from .resources.tasks.client import AsyncTasksClient, TasksClient
from .resources.threads.client import AsyncThreadsClient, ThreadsClient
from .resources.webhooks.client import AsyncWebhooksClient, WebhooksClient
from .resources.workspace_members.client import AsyncWorkspaceMembersClient, WorkspaceMembersClient


class attio_api:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: attio_apiEnvironment = attio_apiEnvironment.PRODUCTION,
        token: typing.Union[str, typing.Callable[[], str]],
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None
    ):
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            token=token,
            httpx_client=httpx.Client(timeout=timeout) if httpx_client is None else httpx_client,
        )
        self.objects = ObjectsClient(client_wrapper=self._client_wrapper)
        self.attributes = AttributesClient(client_wrapper=self._client_wrapper)
        self.records = RecordsClient(client_wrapper=self._client_wrapper)
        self.lists = ListsClient(client_wrapper=self._client_wrapper)
        self.entries = EntriesClient(client_wrapper=self._client_wrapper)
        self.workspace_members = WorkspaceMembersClient(client_wrapper=self._client_wrapper)
        self.notes = NotesClient(client_wrapper=self._client_wrapper)
        self.tasks = TasksClient(client_wrapper=self._client_wrapper)
        self.threads = ThreadsClient(client_wrapper=self._client_wrapper)
        self.comments = CommentsClient(client_wrapper=self._client_wrapper)
        self.webhooks = WebhooksClient(client_wrapper=self._client_wrapper)
        self.meta = MetaClient(client_wrapper=self._client_wrapper)


class Asyncattio_api:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: attio_apiEnvironment = attio_apiEnvironment.PRODUCTION,
        token: typing.Union[str, typing.Callable[[], str]],
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None
    ):
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            token=token,
            httpx_client=httpx.AsyncClient(timeout=timeout) if httpx_client is None else httpx_client,
        )
        self.objects = AsyncObjectsClient(client_wrapper=self._client_wrapper)
        self.attributes = AsyncAttributesClient(client_wrapper=self._client_wrapper)
        self.records = AsyncRecordsClient(client_wrapper=self._client_wrapper)
        self.lists = AsyncListsClient(client_wrapper=self._client_wrapper)
        self.entries = AsyncEntriesClient(client_wrapper=self._client_wrapper)
        self.workspace_members = AsyncWorkspaceMembersClient(client_wrapper=self._client_wrapper)
        self.notes = AsyncNotesClient(client_wrapper=self._client_wrapper)
        self.tasks = AsyncTasksClient(client_wrapper=self._client_wrapper)
        self.threads = AsyncThreadsClient(client_wrapper=self._client_wrapper)
        self.comments = AsyncCommentsClient(client_wrapper=self._client_wrapper)
        self.webhooks = AsyncWebhooksClient(client_wrapper=self._client_wrapper)
        self.meta = AsyncMetaClient(client_wrapper=self._client_wrapper)


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: attio_apiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")