from datetime import datetime
from typing import Optional

from core.application.dtos.base import BaseRequest, BaseResponse

class CreateQuestionRequestDto(BaseRequest):
    quiz_id: int
    content: str
    display_order: int

class UpdateQuestionRequestDto(BaseRequest):
    quiz_id: Optional[int] = None
    content: Optional[str] = None
    display_order: Optional[int] = None

class QuestionResponseDto(BaseResponse):
    id: int
    quiz_id: int
    content: str
    display_order: int
    created_at: datetime
    updated_at: datetime