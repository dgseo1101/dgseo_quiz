from datetime import datetime
from typing import Optional

from core.application.dtos.base import BaseRequest, BaseResponse

class CreateQuizAttemptRequestDto(BaseRequest):
    quiz_id: int
    user_id: int

class UpdateQuizAttemptRequestDto(BaseRequest):
    quiz_id: Optional[int] = None
    user_id: Optional[int] = None

class QuizAttemptResponseDto(BaseResponse):
    id: int
    quiz_id: int
    user_id: int
    created_at: datetime
    updated_at: datetime