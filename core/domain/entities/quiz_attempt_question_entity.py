from datetime import datetime
from typing import Optional

from core.domain.entities.entity import Entity

class CreateQuizAttemptQuestionEntity(Entity):
    quiz_attempt_id: int
    question_id: int
    question_order: int
    selected_choice_id: Optional[int] = None

class UpdateQuizAttemptQuestionEntity(Entity):
    quiz_attempt_id: Optional[int] = None
    question_id: Optional[int] = None
    question_order: Optional[int] = None
    selected_choice_id: Optional[int] = None

class QuizAttemptQuestionEntity(Entity):
    id: int
    quiz_attempt_id: int
    question_id: int
    question_order: int
    selected_choice_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime