from contextlib import AbstractAsyncContextManager
from typing import Callable, List

from sqlalchemy import select, update, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from core.infrastructure.database.models.quiz_attempt_model import QuizAttemptModel
from core.infrastructure.repositories.base_repository import BaseRepository

from core.infrastructure.database.models.quiz_attempt_question_model import QuizAttemptQuestionModel
from core.infrastructure.database.models.attempt_seed_model import AttempSeedModel

from core.domain.entities.quiz_attempt_entity import (
    QuizAttemptEntity,
    CreateQuizAttemptEntity,
    UpdateQuizAttemptEntity,
)

from server.application.dtos.quiz_attempt_dto import (
    AnswerSubmissionDto,
    QuizAttemptWithSeedResponseDto
)

SessionFactory = Callable[..., AbstractAsyncContextManager[AsyncSession]]


class QuizAttemptRepository(BaseRepository):
    def __init__(self, session: SessionFactory) -> None:
        self.session = session

    @property
    def model(self):
        return QuizAttemptModel 

    @property
    def create_entity(self):
        return CreateQuizAttemptEntity

    @property
    def return_entity(self):
        return QuizAttemptEntity

    @property
    def update_entity(self):
        # 업데이트 시 사용하는 엔티티나 로직
        return UpdateQuizAttemptEntity
    
    async def get_data_by_user_id(self, user_id: int):
        async with self.session() as session:
            result = await session.execute(
                select(QuizAttemptModel, AttempSeedModel)
                .where(QuizAttemptModel.user_id == user_id)
                .join(AttempSeedModel, QuizAttemptModel.id == AttempSeedModel.quiz_attempt_id, isouter=True)
            )
            datas = result.all()

        return [QuizAttemptWithSeedResponseDto(
            id=attempt.id,
            user_id=attempt.user_id,
            quiz_id=attempt.quiz_id,
            seed= seed.seed,
            created_at=attempt.created_at,
            updated_at=attempt.updated_at
        ) for attempt, seed in datas]
    
    async def update_attempt_answers(self, attempt_id: int, answers: List[AnswerSubmissionDto]) -> None:
        async with self.session() as session:
            for ans in answers:
                stmt = (
                    update(QuizAttemptQuestionModel)
                    .where(
                        QuizAttemptQuestionModel.id == ans.quiz_attempt_question_id
                    )
                    .values(selected_choice_id=ans.selected_choice_id)
                )
                await session.execute(stmt)
            await session.commit()

    async def get_attempt_with_details(self, attempt_id: int):
        async with self.session() as session:
            stmt = (
                select(QuizAttemptModel)
                .where(QuizAttemptModel.id == attempt_id)
                .options(
                    selectinload(QuizAttemptModel.attempt_questions)
                    .selectinload(QuizAttemptQuestionModel.selected_choice),
                    selectinload(QuizAttemptModel.attempt_questions)
                    .selectinload(QuizAttemptQuestionModel.question)
                )
            )
            result = await session.execute(stmt)
        return result.scalar_one_or_none()
    
    async def add_attempt_questions(self, attempt: QuizAttemptModel, questions: List):
        async with self.session() as session:
            for i, question in enumerate(questions):
                aq = QuizAttemptQuestionModel(
                    id=attempt.id,
                    question_id=question.id,
                    question_order=i
                )
                attempt.attempt_questions.append(aq)
            session.add(attempt)
            await session.commit()
            await session.refresh(attempt)

            return attempt