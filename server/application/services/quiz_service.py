# -*- coding: utf-8 -*-
import logging
import random

from typing import Optional

from core.application.dtos.quiz_dto import (
    CreateQuizRequestDto,
    QuizResponseDto,
    UpdateQuizRequestDto,
)
from core.application.services.base_service import BaseService
from server.infrastructure.repositories.quiz_repository import QuizRepository

from fastapi import HTTPException

from server.application.dtos.quiz_dto import (
    QuizCreate,
    ChoiceResponseDto,
    QuestionWithChoiceResponseDto,
    QuizDetailResponseDto
)
from core.infrastructure.database.models.quiz_model import QuizModel
from core.infrastructure.database.models.question_model import QuestionModel
from core.infrastructure.database.models.choice_model import ChoiceModel

class QuizService(BaseService):
    def __init__(self, quiz_repository: QuizRepository) -> None:
        super().__init__(base_repository=quiz_repository)
        self.logger = logging.getLogger(__name__)
        self.quiz_repository = quiz_repository

    @property
    def create_dto(self):
        return CreateQuizRequestDto

    @property
    def response_dto(self):
        return QuizResponseDto

    @property
    def update_dto(self):
        return UpdateQuizRequestDto
    
    async def create_quiz(self, create_data: QuizCreate, user_id: int):
        for question in create_data.questions:
            if len(question.choices) != question.n + 2 :
                raise HTTPException(status_code=400, detail=f"각 문제는 {question.n + 2 }개의 선택지를 가져야 합니다.")
            correct_count = sum(1 for choice in question.choices if choice.is_correct)
            if correct_count != 1:
                raise HTTPException(status_code=400, detail="각 문제는 반드시 정답 선택지가 1개여야 합니다.")
        
        quiz = QuizModel(
            title=create_data.title,
            description=create_data.description,
            randomize_questions=create_data.randomize_questions,
            randomize_choices=create_data.randomize_choices,
            num_questions_to_display=create_data.num_questions_to_display,
            created_by=user_id
        )

        for q in create_data.questions:
            question_model = QuestionModel(
                content=q.content,
                display_order=q.display_order
            )

            for idx, choice_data in enumerate(q.choices):
                choice_model = ChoiceModel(
                    content=choice_data.content,
                    is_correct=choice_data.is_correct,
                    display_order=idx
                )
                question_model.choices.append(choice_model)

            quiz.questions.append(question_model)

        return await self.quiz_repository.create_data_orm(create_data=quiz)
    
    async def get_quiz(self, quiz_id: int, page: int, page_size: int, seed: Optional[int] = None):
        quiz = await self.quiz_repository.get_quiz_with_questions(quiz_id)
        if not quiz:
            raise HTTPException(status_code=404, detail="Quiz not found")
        
        if seed is None:
            seed = random.randint(1, 1000000)

        rng = random.Random(seed)
        
        total_questions = quiz.questions or []
        if len(total_questions) > quiz.num_questions_to_display:
            selected_questions = rng.sample(total_questions, quiz.num_questions_to_display)
        else:
            selected_questions = total_questions.copy()
        
        if quiz.randomize_questions:
            rng.shuffle(selected_questions)
        
        start_idx = (page - 1) * page_size
        end_idx = start_idx + page_size
        paginated_questions = selected_questions[start_idx:end_idx]

        for question in paginated_questions:
            if quiz.randomize_choices:
                random.shuffle(question.choices)

        question_dtos = []
        for question in paginated_questions:
            choice_dtos = [
                ChoiceResponseDto(
                    choice_id=choice.id,
                    content=choice.content,
                )
                for choice in question.choices
            ]
            question_dto = QuestionWithChoiceResponseDto(
                question_id=question.id,
                content=question.content,
                choices=choice_dtos
            )
            question_dtos.append(question_dto)

        response_dto = QuizDetailResponseDto(
            quiz_id=quiz.id,
            title=quiz.title,
            description=quiz.description,
            created_at=quiz.created_at,
            updated_at=quiz.updated_at,
            total_selected_questions=len(selected_questions),
            page=page,
            page_size=page_size,
            questions=question_dtos,
            seed=seed
        )
        
        return response_dto