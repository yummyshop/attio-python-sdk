# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class OauthScope(str, enum.Enum):
    USER_MANAGEMENT_READ = "user_management:read"
    """
    View workspace members.
    """

    USER_MANAGEMENT_READ_WRITE = "user_management:read-write"
    """
    View workspace members.
    """

    RECORD_PERMISSION_READ = "record_permission:read"
    """
    View, and optionally write, records.
    """

    RECORD_PERMISSION_READ_WRITE = "record_permission:read-write"
    """
    View, and optionally write, records.
    """

    OBJECT_CONFIGURATION_READ = "object_configuration:read"
    """
    View, and optionally write, the configuration and attributes of objects.
    """

    OBJECT_CONFIGURATION_READ_WRITE = "object_configuration:read-write"
    """
    View, and optionally write, the configuration and attributes of objects.
    """

    LIST_ENTRY_READ = "list_entry:read"
    """
    View, and optionally write, the entries in a list.
    """

    LIST_ENTRY_READ_WRITE = "list_entry:read-write"
    """
    View, and optionally write, the entries in a list.
    """

    LIST_CONFIGURATION_READ = "list_configuration:read"
    """
    View, and optionally write, the configuration and attributes of lists.
    """

    LIST_CONFIGURATION_READ_WRITE = "list_configuration:read-write"
    """
    View, and optionally write, the configuration and attributes of lists.
    """

    PUBLIC_COLLECTION_READ = "public_collection:read"
    """
    View, and optionally write, both the settings and information within public collections.
    """

    PUBLIC_COLLECTION_READ_WRITE = "public_collection:read-write"
    """
    View, and optionally write, both the settings and information within public collections.
    """

    PRIVATE_COLLECTION_READ = "private_collection:read"
    """
    View, and optionally modify, both the settings and information of all collections within the workspace, regardless of their access settings.
    """

    PRIVATE_COLLECTION_READ_WRITE = "private_collection:read-write"
    """
    View, and optionally modify, both the settings and information of all collections within the workspace, regardless of their access settings.
    """

    COMMENT_READ = "comment:read"
    """
    View comments (and threads), and optionally write comments.
    """

    COMMENT_READ_WRITE = "comment:read-write"
    """
    View comments (and threads), and optionally write comments.
    """

    TASK_READ = "task:read"
    """
    View, and optionally write, tasks.
    """

    TASK_READ_WRITE = "task:read-write"
    """
    View, and optionally write, tasks.
    """

    NOTE_READ = "note:read"
    """
    View, and optionally write, notes.
    """

    NOTE_READ_WRITE = "note:read-write"
    """
    View, and optionally write, notes.
    """

    WEBHOOK_READ = "webhook:read"
    """
    View, and optionally manage, webhooks.
    """

    WEBHOOK_READ_WRITE = "webhook:read-write"
    """
    View, and optionally manage, webhooks.
    """

    def visit(
        self,
        user_management_read: typing.Callable[[], T_Result],
        user_management_read_write: typing.Callable[[], T_Result],
        record_permission_read: typing.Callable[[], T_Result],
        record_permission_read_write: typing.Callable[[], T_Result],
        object_configuration_read: typing.Callable[[], T_Result],
        object_configuration_read_write: typing.Callable[[], T_Result],
        list_entry_read: typing.Callable[[], T_Result],
        list_entry_read_write: typing.Callable[[], T_Result],
        list_configuration_read: typing.Callable[[], T_Result],
        list_configuration_read_write: typing.Callable[[], T_Result],
        public_collection_read: typing.Callable[[], T_Result],
        public_collection_read_write: typing.Callable[[], T_Result],
        private_collection_read: typing.Callable[[], T_Result],
        private_collection_read_write: typing.Callable[[], T_Result],
        comment_read: typing.Callable[[], T_Result],
        comment_read_write: typing.Callable[[], T_Result],
        task_read: typing.Callable[[], T_Result],
        task_read_write: typing.Callable[[], T_Result],
        note_read: typing.Callable[[], T_Result],
        note_read_write: typing.Callable[[], T_Result],
        webhook_read: typing.Callable[[], T_Result],
        webhook_read_write: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OauthScope.USER_MANAGEMENT_READ:
            return user_management_read()
        if self is OauthScope.USER_MANAGEMENT_READ_WRITE:
            return user_management_read_write()
        if self is OauthScope.RECORD_PERMISSION_READ:
            return record_permission_read()
        if self is OauthScope.RECORD_PERMISSION_READ_WRITE:
            return record_permission_read_write()
        if self is OauthScope.OBJECT_CONFIGURATION_READ:
            return object_configuration_read()
        if self is OauthScope.OBJECT_CONFIGURATION_READ_WRITE:
            return object_configuration_read_write()
        if self is OauthScope.LIST_ENTRY_READ:
            return list_entry_read()
        if self is OauthScope.LIST_ENTRY_READ_WRITE:
            return list_entry_read_write()
        if self is OauthScope.LIST_CONFIGURATION_READ:
            return list_configuration_read()
        if self is OauthScope.LIST_CONFIGURATION_READ_WRITE:
            return list_configuration_read_write()
        if self is OauthScope.PUBLIC_COLLECTION_READ:
            return public_collection_read()
        if self is OauthScope.PUBLIC_COLLECTION_READ_WRITE:
            return public_collection_read_write()
        if self is OauthScope.PRIVATE_COLLECTION_READ:
            return private_collection_read()
        if self is OauthScope.PRIVATE_COLLECTION_READ_WRITE:
            return private_collection_read_write()
        if self is OauthScope.COMMENT_READ:
            return comment_read()
        if self is OauthScope.COMMENT_READ_WRITE:
            return comment_read_write()
        if self is OauthScope.TASK_READ:
            return task_read()
        if self is OauthScope.TASK_READ_WRITE:
            return task_read_write()
        if self is OauthScope.NOTE_READ:
            return note_read()
        if self is OauthScope.NOTE_READ_WRITE:
            return note_read_write()
        if self is OauthScope.WEBHOOK_READ:
            return webhook_read()
        if self is OauthScope.WEBHOOK_READ_WRITE:
            return webhook_read_write()