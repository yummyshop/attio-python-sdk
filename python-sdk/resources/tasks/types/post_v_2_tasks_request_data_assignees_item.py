# This file was auto-generated by Fern from our API Definition.

import typing

from .post_v_2_tasks_request_data_assignees_item_referenced_actor_id import (
    PostV2TasksRequestDataAssigneesItemReferencedActorId,
)
from .post_v_2_tasks_request_data_assignees_item_workspace_member_email_address import (
    PostV2TasksRequestDataAssigneesItemWorkspaceMemberEmailAddress,
)

PostV2TasksRequestDataAssigneesItem = typing.Union[
    PostV2TasksRequestDataAssigneesItemReferencedActorId, PostV2TasksRequestDataAssigneesItemWorkspaceMemberEmailAddress
]