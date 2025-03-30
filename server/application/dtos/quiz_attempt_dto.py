from datetime import datetime

from typing import Optional, List

from core.application.dtos.base import BaseRequest, BaseResponse

class AnswerSubmissionDto(BaseRequest):
    quiz_attempt_question_id: int
    selected_choice_id: int

class QuizSubmitRequestDto(BaseRequest):
    answers: List[AnswerSubmissionDto]

class QuizSubmitResponseDto(BaseRequest):
    attempt_id: int
    score: int

class QuizAttemptWithSeedResponseDto(BaseResponse):
    id: int
    user_id: int
    quiz_id: int
    seed: int
    created_at: datetime
    updated_at: datetime