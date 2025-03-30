from datetime import datetime
from typing import Optional

from core.application.dtos.base import BaseRequest, BaseResponse

class CreateQuizAttemptQuestionRequestDto(BaseRequest):
    quiz_attempt_id: int
    question_id: int
    question_order: int
    selected_choice_id: Optional[int] = None

class UpdateQuizAttemptQuestionRequestDto(BaseRequest):
    quiz_attempt_id: Optional[int] = None
    question_id: Optional[int] = None
    question_order: Optional[int] = None
    selected_choice_id: Optional[int] = None

class QuizAttemptQuestionResponseDto(BaseResponse):
    id: int
    quiz_attempt_id: int
    question_id: int
    question_order: int
    selected_choice_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime