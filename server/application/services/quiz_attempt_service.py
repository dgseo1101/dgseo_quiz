# -*- coding: utf-8 -*-
import logging
import random

from fastapi import HTTPException

from core.application.dtos.quiz_attempt_dto import (
    CreateQuizAttemptRequestDto,
    QuizAttemptResponseDto,
    UpdateQuizAttemptRequestDto,
)
from core.application.services.base_service import BaseService
from server.infrastructure.repositories.quiz_attempt_repository import QuizAttemptRepository
from server.infrastructure.repositories.quiz_repository import QuizRepository
from server.infrastructure.repositories.quiz_attempt_question_repository import QuizAttemptQuestionRepository
from server.infrastructure.repositories.attempt_seed_repository import AttemptSeedRepository

from core.application.dtos.attempt_seed_dto import CreateAttemptSeedRequestDto

from core.application.dtos.quiz_attempt_question_dto import CreateQuizAttemptQuestionRequestDto

from server.application.dtos.quiz_attempt_dto import (
    QuizSubmitResponseDto,
    QuizSubmitRequestDto
)


class QuizAttemptService(BaseService):
    def __init__(self, 
                 quiz_attempt_repository: QuizAttemptRepository,
                 quiz_repository: QuizRepository,
                 quiz_attempt_question_repository: QuizAttemptQuestionRepository,
                 attempt_seed_repository: AttemptSeedRepository) -> None:
        super().__init__(base_repository=quiz_attempt_repository)
        self.logger = logging.getLogger(__name__)
        self.quiz_attempt_repository = quiz_attempt_repository
        self.quiz_repository = quiz_repository
        self.quiz_attempt_question_repository = quiz_attempt_question_repository
        self.attempt_seed_repository = attempt_seed_repository

    @property
    def create_dto(self):
        return CreateQuizAttemptRequestDto

    @property
    def response_dto(self):
        return QuizAttemptResponseDto

    @property
    def update_dto(self):
        return UpdateQuizAttemptRequestDto
    
    async def get_quiz_attempt(self, user_id: int):
        return await self.quiz_attempt_repository.get_data_by_user_id(user_id = user_id)
    
    async def start_quiz_attempt(self, quiz_id: int, user_id: int, seed: int):
        quiz = await self.quiz_repository.get_quiz_with_questions(quiz_id)
        if not quiz:
            raise HTTPException(status_code=404, detail="Quiz not found")

        total_questions = quiz.questions or []

        create_data = CreateQuizAttemptRequestDto(
            user_id = user_id,
            quiz_id = quiz_id
        )

        attempt = await self.quiz_attempt_repository.create_data(create_data=create_data)

        seed_create_data = CreateAttemptSeedRequestDto(
            quiz_attempt_id=attempt.id,
            seed=seed
        )

        await self.attempt_seed_repository.create_data(create_data=seed_create_data)

        attempt_question_create_datas = []
        for i, question in enumerate(total_questions):
            attempt_question_create_datas.append(
                CreateQuizAttemptQuestionRequestDto(
                    quiz_attempt_id=attempt.id,
                    question_id=question.id,
                    question_order=i
                )
            )

        attempt = await self.quiz_attempt_question_repository.create_datas(create_datas=attempt_question_create_datas)
        return attempt

    async def submit_quiz_attempt(self, attempt_id: int, submission: QuizSubmitRequestDto) -> QuizSubmitResponseDto:
        await self.quiz_attempt_repository.update_attempt_answers(attempt_id, submission.answers)
        attempt = await self.quiz_attempt_repository.get_attempt_with_details(attempt_id)
        if not attempt:
            raise HTTPException(status_code=404, detail="Attempt not found")

        score = 0
        for aq in attempt.attempt_questions:
            if aq.selected_choice and aq.selected_choice.is_correct:
                score += 1

        return QuizSubmitResponseDto(attempt_id=attempt.id, score=score)