from datetime import datetime
from typing import Optional

from core.domain.entities.entity import Entity

class CreateQuizAttemptEntity(Entity):
    quiz_id: int
    user_id: int

class UpdateQuizAttemptEntity(Entity):
    quiz_id: Optional[int] = None
    user_id: Optional[int] = None

class QuizAttemptEntity(Entity):
    id: int
    quiz_id: int
    user_id: int
    created_at: datetime
    updated_at: datetime