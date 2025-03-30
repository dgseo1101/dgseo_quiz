# -*- coding: utf-8 -*-
import logging

from core.application.dtos.quiz_attempt_question_dto import (
    CreateQuizAttemptQuestionRequestDto,
    QuizAttemptQuestionResponseDto,
    UpdateQuizAttemptQuestionRequestDto,
)
from core.application.services.base_service import BaseService
from server.infrastructure.repositories.quiz_attempt_question_repository import QuizAttemptQuestionRepository


class QuizAttemptQuestionService(BaseService):
    def __init__(self, quiz_attempt_question_repository: QuizAttemptQuestionRepository) -> None:
        super().__init__(base_repository=quiz_attempt_question_repository)
        self.logger = logging.getLogger(__name__)
        self.quiz_attempt_question_repository = quiz_attempt_question_repository

    @property
    def create_dto(self):
        return CreateQuizAttemptQuestionRequestDto

    @property
    def response_dto(self):
        return QuizAttemptQuestionResponseDto

    @property
    def update_dto(self):
        return UpdateQuizAttemptQuestionRequestDto
