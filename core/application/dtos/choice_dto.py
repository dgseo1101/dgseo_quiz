from datetime import datetime
from typing import Optional

from core.application.dtos.base import BaseRequest, BaseResponse

class CreateChoiceRequestDto(BaseRequest):
    question_id: int
    content: str
    is_correct: bool
    display_order: int

class UpdateChoiceRequestDto(BaseRequest):
    question_id: Optional[int] = None
    content: Optional[str] = None
    is_correct: Optional[bool] = None
    display_order: Optional[int] = None

class ChoiceResponseDto(BaseResponse):
    id: int
    question_id: int
    content: str
    is_correct: bool
    display_order: int
    created_at: datetime
    updated_at: datetime
