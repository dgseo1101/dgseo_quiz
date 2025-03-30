from datetime import datetime
from typing import Optional

from core.domain.entities.entity import Entity

class CreateAssignmentEntity(Entity):
    user_id: int
    quiz_id: int

class UpdateAssignmentEntity(Entity):
    user_id: int
    quiz_id: int

class AssignmentEntity(Entity):
    id: int
    user_id: int
    quiz_id: int
    created_at: datetime
    updated_at: datetime