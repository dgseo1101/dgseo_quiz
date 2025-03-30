from datetime import datetime

from typing import List, Optional

from core.application.dtos.base import BaseRequest, BaseResponse

class ChoiceCreate(BaseRequest):
    content: str
    is_correct: bool

class QuestionCreate(BaseRequest):
    n: int
    content: str
    display_order: Optional[int] = None
    choices: List[ChoiceCreate]

class QuizCreate(BaseRequest):
    title: str
    description: Optional[str] = None
    randomize_questions: bool = False
    randomize_choices: bool = False
    num_questions_to_display: int
    questions: List[QuestionCreate]

class ChoiceResponseDto(BaseResponse):
    choice_id: int
    content: str

class QuestionWithChoiceResponseDto(BaseResponse):
    question_id: int
    content: str
    choices: List[ChoiceResponseDto]

class QuizDetailResponseDto(BaseResponse):
    quiz_id: int
    title: str
    description: Optional[str]
    created_at: datetime
    updated_at: datetime
    total_selected_questions: int
    page: int
    page_size: int
    questions: List[QuestionWithChoiceResponseDto]
    seed: int