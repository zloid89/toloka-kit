__all__ = [
    'Assignment',
    'AssignmentPatch',
    'GetAssignmentsTsvParameters'
]
from attr.validators import optional, instance_of
import datetime
from decimal import Decimal
from enum import unique
from typing import List, Optional

from .primitives.base import BaseTolokaObject
from .primitives.parameter import Parameters
from .solution import Solution
from .task import Task
from ..util._codegen import attribute
from ..util._extendable_enum import ExtendableStrEnum


class Assignment(BaseTolokaObject):
    """Information about an assigned task suite.

    Attributes:
        id: The ID of the assignment.
        task_suite_id: The ID of the assigned task suite.
        pool_id: The ID of the pool containing the task suite.
        user_id: The ID of the performer who was assigned the task suite.
        status: Status of the assignment.
            * `ACTIVE` — The task suite is assigned but it isn't completed yet.
            * `SUBMITTED` — The task suite is completed but it isn't checked.
            * `ACCEPTED` — The task suite is accepted by the requester.
            * `REJECTED` — The task suite is rejected by the requester.
            * `SKIPPED` — The task suite is skipped by the performer.
            * `EXPIRED` — Time for completing the tasks has expired.
        reward: Payment received by the performer.
        tasks: All tasks in the task suite.
        automerged: A flag showing merged tasks:
            * `True` — The response was obtained by merging identical tasks.
            * `False` — No task merging occurred.
        created: The date and time when the task suite was assigned to the performer.
        submitted: The date and time when the task suite was completed by the performer.
        accepted: The date and time when the responses for the task suite were accepted by the requester.
        rejected: The date and time when the responses for the task suite were rejected by the requester.
        skipped: The date and time when the task suite was skipped by the performer.
        expired: The date and time when time for completing the task suite expired.
        first_declined_solution_attempt: The performer's first try responses in training tasks if the responses are wrong. If the performer answers correctly on the first try, the
            `first_declined_solution_attempt` is omitted.
            The order of the responses is the same as the order of `tasks`.
        solutions: The performer's responses. The order of the responses is the same as the order of `tasks`.
        mixed: The method of grouping tasks in the task suite:
            * `True` — Smart mixing was used.
            * `False` — The tasks were grouped manually, smart mixing was not used.
        public_comment: A public comment that is set when accepting or rejecting the assignment.
    """

    @unique
    class Status(ExtendableStrEnum):
        ACTIVE = 'ACTIVE'
        SUBMITTED = 'SUBMITTED'
        ACCEPTED = 'ACCEPTED'
        REJECTED = 'REJECTED'
        SKIPPED = 'SKIPPED'
        EXPIRED = 'EXPIRED'

    ACTIVE = Status.ACTIVE
    SUBMITTED = Status.SUBMITTED
    ACCEPTED = Status.ACCEPTED
    REJECTED = Status.REJECTED
    SKIPPED = Status.SKIPPED
    EXPIRED = Status.EXPIRED

    id: str
    task_suite_id: str
    pool_id: str
    user_id: str
    status: Status = attribute(autocast=True)
    reward: Decimal = attribute(validator=optional(instance_of(Decimal)))
    tasks: List[Task]
    automerged: bool

    created: datetime.datetime
    submitted: datetime.datetime
    accepted: datetime.datetime
    rejected: datetime.datetime
    skipped: datetime.datetime
    expired: datetime.datetime

    first_declined_solution_attempt: List[Solution]
    solutions: List[Solution]
    mixed: bool

    public_comment: str


class AssignmentPatch(BaseTolokaObject):
    """The new status of an assignment.

    It is used in the [patch_assignment](toloka.client.TolokaClient.patch_assignment.md) method to accept or reject an assignment and to leave a comment.

    Attributes:
        public_comment: The public comment.
        status: The new status of an assignment:
            * `ACCEPTED` — Accepted by the requester.
            * `REJECTED` — Rejected by the requester.
    """
    public_comment: str
    status: Assignment.Status


class GetAssignmentsTsvParameters(Parameters):
    """Parameters for downloading assignments.

    These parameters are used in the [TolokaClient.get_assignments_df](toloka.client.TolokaClient.get_assignments_df.md) method.

    Attributes:
        status: Statuses of assignments to download.
        start_time_from: Download assignments submitted after the specified date and time.
        start_time_to: Download assignments submitted before the specified date and time.
        exclude_banned: Exclude answers from banned performers, even if their assignments have suitable status.
        field: Names of `Assignment` fields to be downloaded. Fields other then from `Assignment` class are always downloaded.
    """

    @unique
    class Status(ExtendableStrEnum):
        ACTIVE = 'ACTIVE'
        SUBMITTED = 'SUBMITTED'
        APPROVED = 'APPROVED'
        REJECTED = 'REJECTED'
        SKIPPED = 'SKIPPED'
        EXPIRED = 'EXPIRED'

    @unique
    class Field(ExtendableStrEnum):
        LINK = 'ASSIGNMENT:link'
        ASSIGNMENT_ID = 'ASSIGNMENT:assignment_id'
        TASK_ID = 'ASSIGNMENT:task_id'
        TASK_SUITE_ID = 'ASSIGNMENT:task_suite_id'
        WORKER_ID = 'ASSIGNMENT:worker_id'
        STATUS = 'ASSIGNMENT:status'
        STARTED = 'ASSIGNMENT:started'
        SUBMITTED = 'ASSIGNMENT:submitted'
        ACCEPTED = 'ASSIGNMENT:accepted'
        REJECTED = 'ASSIGNMENT:rejected'
        SKIPPED = 'ASSIGNMENT:skipped'
        EXPIRED = 'ASSIGNMENT:expired'
        REWARD = 'ASSIGNMENT:reward'

    _default_status = [Status.APPROVED]
    _default_fields = [Field.LINK, Field.ASSIGNMENT_ID, Field.WORKER_ID, Field.STATUS, Field.STARTED]

    status: List[Status] = attribute(factory=lambda: GetAssignmentsTsvParameters._default_status)
    start_time_from: Optional[datetime.datetime] = attribute(origin='startTimeFrom')
    start_time_to: Optional[datetime.datetime] = attribute(origin='startTimeTo')
    exclude_banned: Optional[bool] = attribute(origin='excludeBanned')
    field: List[Field] = attribute(
        factory=lambda: GetAssignmentsTsvParameters._default_fields
    )

    @classmethod
    def structure(cls, data):
        raise NotImplementedError

    def unstructure(self) -> dict:
        data = super().unstructure()
        data['status'] = ','.join(data['status'])
        data['field'] = ','.join(data['field'])
        data['addRowDelimiter'] = False
        return data
