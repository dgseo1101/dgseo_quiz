# -*- coding: utf-8 -*-
import logging

from fastapi import HTTPException

from core.application.dtos.question_dto import (
    CreateQuestionRequestDto,
    QuestionResponseDto,
    UpdateQuestionRequestDto,
)
from core.application.services.base_service import BaseService
from server.infrastructure.repositories.question_repository import QuestionRepository
from core.infrastructure.database.models.question_model import QuestionModel
from core.infrastructure.database.models.choice_model import ChoiceModel

from server.application.dtos.quiz_dto import (
    QuestionCreate
)

class QuestionService(BaseService):
    def __init__(self, question_repository: QuestionRepository) -> None:
        super().__init__(base_repository=question_repository)
        self.logger = logging.getLogger(__name__)
        self.question_repository = question_repository

    @property
    def create_dto(self):
        return CreateQuestionRequestDto

    @property
    def response_dto(self):
        return QuestionResponseDto

    @property
    def update_dto(self):
        return UpdateQuestionRequestDto

    async def create_question(self, quiz_id: int,create_data: QuestionCreate):
        if len(create_data.choices) != create_data.n + 2:
            raise HTTPException(status_code=400, detail=f"각 문제는 {create_data.n + 2 }개의 선택지를 가져야 합니다.")
        correct_count = sum(1 for choice in create_data.choices if choice.is_correct)
        if correct_count != 1:
            raise HTTPException(status_code=400, detail="각 문제는 반드시 정답 선택지가 1개여야 합니다.")
        
        question_model = QuestionModel(
            quiz_id=quiz_id,
            content=create_data.content,
            display_order=create_data.display_order
        )

        for idx, choice_data in enumerate(create_data.choices):
            choice_model = ChoiceModel(
                content=choice_data.content,
                is_correct=choice_data.is_correct,
                display_order=idx
            )

            question_model.choices.append(choice_model)

        return await self.question_repository.create_data_orm(create_data=question_model)