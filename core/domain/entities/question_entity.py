from datetime import datetime
from typing import Optional

from core.domain.entities.entity import Entity

class CreateQuestionEntity(Entity):
    quiz_id: int
    content: str
    display_order: int

class UpdateQuestionEntity(Entity):
    quiz_id: Optional[int] = None
    content: Optional[str] = None
    display_order: Optional[int] = None

class QuestionEntity(Entity):
    id: int
    quiz_id: int
    content: str
    display_order: int
    created_at: datetime
    updated_at: datetime