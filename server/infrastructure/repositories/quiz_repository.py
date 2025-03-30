from contextlib import AbstractAsyncContextManager
from typing import Callable, Optional, List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from core.infrastructure.database.models.quiz_model import QuizModel
from core.infrastructure.database.models.assignment_model import AssignmentModel
from core.infrastructure.repositories.base_repository import BaseRepository

from core.domain.entities.quiz_entity import (
    QuizEntity,
    CreateQuizEntity,
    UpdateQuizEntity,
)

from core.infrastructure.database.models.question_model import QuestionModel

SessionFactory = Callable[..., AbstractAsyncContextManager[AsyncSession]]


class QuizRepository(BaseRepository):
    def __init__(self, session: SessionFactory) -> None:
        self.session = session

    @property
    def model(self):
        return QuizModel 

    @property
    def create_entity(self):
        return CreateQuizEntity

    @property
    def return_entity(self):
        return QuizEntity

    @property
    def update_entity(self):
        return UpdateQuizEntity
    
    async def get_data_by_user_id(self, user_id: int, page: int, page_size: int) -> List[QuizEntity]:
        async with self.session() as session:
            offset = (page - 1) * page_size
            stmt = (
                select(QuizModel)
                .join(AssignmentModel, AssignmentModel.quiz_id == QuizModel.id)
                .where(AssignmentModel.user_id == user_id)
                .offset(offset)
                .limit(page_size)
            )
            result = await session.execute(stmt)
            quizzes = result.scalars().all()
            return quizzes
    
    async def get_quiz_with_questions(self, quiz_id: int) -> Optional[QuizModel]:
        async with self.session() as session:
            stmt = (
                select(QuizModel)
                .where(QuizModel.id == quiz_id)
                .options(
                    selectinload(QuizModel.questions)
                    .selectinload(QuestionModel.choices)
                )
            )
            result = await session.execute(stmt)
        return result.scalar_one_or_none()