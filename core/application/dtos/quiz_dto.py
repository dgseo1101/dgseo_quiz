from datetime import datetime
from typing import Optional

from core.application.dtos.base import BaseRequest, BaseResponse

class CreateQuizRequestDto(BaseRequest):
    title: str
    description: str
    created_by: int
    randomize_questions: bool
    randomize_choices: bool
    num_questions_to_display: int
    page_size: int

class UpdateQuizRequestDto(BaseRequest):
    title: Optional[str] = None
    description: Optional[str] = None
    randomize_questions: Optional[bool] = None
    randomize_choices: Optional[bool] = None
    num_questions_to_display: Optional[int] = None
    page_size: Optional[int] = None

class QuizResponseDto(BaseResponse):
    id: int
    title: str
    description: str
    created_by: int
    created_at: datetime
    updated_at: datetime
    randomize_questions: bool
    randomize_choices: bool
    num_questions_to_display: int
    page_size: int