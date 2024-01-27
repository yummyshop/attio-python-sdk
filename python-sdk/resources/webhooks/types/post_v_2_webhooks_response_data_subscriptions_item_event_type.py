# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostV2WebhooksResponseDataSubscriptionsItemEventType(str, enum.Enum):
    """
    Type of event the webhook is subscribed to.
    """

    COMMENT_CREATED = "comment.created"
    COMMENT_RESOLVED = "comment.resolved"
    COMMENT_UNRESOLVED = "comment.unresolved"
    COMMENT_DELETED = "comment.deleted"
    LIST_CREATED = "list.created"
    LIST_UPDATED = "list.updated"
    LIST_DELETED = "list.deleted"
    LIST_ATTRIBUTE_CREATED = "list-attribute.created"
    LIST_ATTRIBUTE_UPDATED = "list-attribute.updated"
    LIST_ENTRY_CREATED = "list-entry.created"
    LIST_ENTRY_UPDATED = "list-entry.updated"
    LIST_ENTRY_DELETED = "list-entry.deleted"
    OBJECT_ATTRIBUTE_CREATED = "object-attribute.created"
    OBJECT_ATTRIBUTE_UPDATED = "object-attribute.updated"
    NOTE_CREATED = "note.created"
    NOTE_UPDATED = "note.updated"
    NOTE_DELETED = "note.deleted"
    RECORD_CREATED = "record.created"
    RECORD_MERGED = "record.merged"
    RECORD_UPDATED = "record.updated"
    RECORD_DELETED = "record.deleted"
    TASK_CREATED = "task.created"
    TASK_UPDATED = "task.updated"
    TASK_DELETED = "task.deleted"
    WORKSPACE_MEMBER_CREATED = "workspace-member.created"

    def visit(
        self,
        comment_created: typing.Callable[[], T_Result],
        comment_resolved: typing.Callable[[], T_Result],
        comment_unresolved: typing.Callable[[], T_Result],
        comment_deleted: typing.Callable[[], T_Result],
        list_created: typing.Callable[[], T_Result],
        list_updated: typing.Callable[[], T_Result],
        list_deleted: typing.Callable[[], T_Result],
        list_attribute_created: typing.Callable[[], T_Result],
        list_attribute_updated: typing.Callable[[], T_Result],
        list_entry_created: typing.Callable[[], T_Result],
        list_entry_updated: typing.Callable[[], T_Result],
        list_entry_deleted: typing.Callable[[], T_Result],
        object_attribute_created: typing.Callable[[], T_Result],
        object_attribute_updated: typing.Callable[[], T_Result],
        note_created: typing.Callable[[], T_Result],
        note_updated: typing.Callable[[], T_Result],
        note_deleted: typing.Callable[[], T_Result],
        record_created: typing.Callable[[], T_Result],
        record_merged: typing.Callable[[], T_Result],
        record_updated: typing.Callable[[], T_Result],
        record_deleted: typing.Callable[[], T_Result],
        task_created: typing.Callable[[], T_Result],
        task_updated: typing.Callable[[], T_Result],
        task_deleted: typing.Callable[[], T_Result],
        workspace_member_created: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostV2WebhooksResponseDataSubscriptionsItemEventType.COMMENT_CREATED:
            return comment_created()
        if self is PostV2WebhooksResponseDataSubscriptionsItemEventType.COMMENT_RESOLVED:
            return comment_resolved()
        if self is PostV2WebhooksResponseDataSubscriptionsItemEventType.COMMENT_UNRESOLVED:
            return comment_unresolved()
        if self is PostV2WebhooksResponseDataSubscriptionsItemEventType.COMMENT_DELETED:
            return comment_deleted()
        if self is PostV2WebhooksResponseDataSubscriptionsItemEventType.LIST_CREATED:
            return list_created()
        if self is PostV2WebhooksResponseDataSubscriptionsItemEventType.LIST_UPDATED:
            return list_updated()
        if self is PostV2WebhooksResponseDataSubscriptionsItemEventType.LIST_DELETED:
            return list_deleted()
        if self is PostV2WebhooksResponseDataSubscriptionsItemEventType.LIST_ATTRIBUTE_CREATED:
            return list_attribute_created()
        if self is PostV2WebhooksResponseDataSubscriptionsItemEventType.LIST_ATTRIBUTE_UPDATED:
            return list_attribute_updated()
        if self is PostV2WebhooksResponseDataSubscriptionsItemEventType.LIST_ENTRY_CREATED:
            return list_entry_created()
        if self is PostV2WebhooksResponseDataSubscriptionsItemEventType.LIST_ENTRY_UPDATED:
            return list_entry_updated()
        if self is PostV2WebhooksResponseDataSubscriptionsItemEventType.LIST_ENTRY_DELETED:
            return list_entry_deleted()
        if self is PostV2WebhooksResponseDataSubscriptionsItemEventType.OBJECT_ATTRIBUTE_CREATED:
            return object_attribute_created()
        if self is PostV2WebhooksResponseDataSubscriptionsItemEventType.OBJECT_ATTRIBUTE_UPDATED:
            return object_attribute_updated()
        if self is PostV2WebhooksResponseDataSubscriptionsItemEventType.NOTE_CREATED:
            return note_created()
        if self is PostV2WebhooksResponseDataSubscriptionsItemEventType.NOTE_UPDATED:
            return note_updated()
        if self is PostV2WebhooksResponseDataSubscriptionsItemEventType.NOTE_DELETED:
            return note_deleted()
        if self is PostV2WebhooksResponseDataSubscriptionsItemEventType.RECORD_CREATED:
            return record_created()
        if self is PostV2WebhooksResponseDataSubscriptionsItemEventType.RECORD_MERGED:
            return record_merged()
        if self is PostV2WebhooksResponseDataSubscriptionsItemEventType.RECORD_UPDATED:
            return record_updated()
        if self is PostV2WebhooksResponseDataSubscriptionsItemEventType.RECORD_DELETED:
            return record_deleted()
        if self is PostV2WebhooksResponseDataSubscriptionsItemEventType.TASK_CREATED:
            return task_created()
        if self is PostV2WebhooksResponseDataSubscriptionsItemEventType.TASK_UPDATED:
            return task_updated()
        if self is PostV2WebhooksResponseDataSubscriptionsItemEventType.TASK_DELETED:
            return task_deleted()
        if self is PostV2WebhooksResponseDataSubscriptionsItemEventType.WORKSPACE_MEMBER_CREATED:
            return workspace_member_created()
