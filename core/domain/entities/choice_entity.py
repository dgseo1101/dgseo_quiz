from datetime import datetime
from typing import Optional

from core.domain.entities.entity import Entity

class CreateChoiceEntity(Entity):
    question_id: int
    content: str
    is_correct: bool
    display_order: int

class UpdateChoiceEntity(Entity):
    question_id: Optional[int] = None
    content: Optional[str] = None
    is_correct: Optional[bool] = None
    display_order: Optional[int] = None

class ChoiceEntity(Entity):
    id: int
    question_id: int
    content: str
    is_correct: bool
    display_order: int
    created_at: datetime
    updated_at: datetime
