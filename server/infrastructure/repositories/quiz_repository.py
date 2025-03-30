from contextlib import AbstractAsyncContextManager
from typing import Callable, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from core.infrastructure.database.models.quiz_model import QuizModel
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
        return QuizModel  # 유저 엔티티를 반환

    @property
    def create_entity(self):
        # 여기에서 필요한 로직으로 엔티티를 생성할 수 있음
        return CreateQuizEntity

    @property
    def return_entity(self):
        # 반환할 때 사용하는 DTO 또는 엔티티 정의
        return QuizEntity

    @property
    def update_entity(self):
        # 업데이트 시 사용하는 엔티티나 로직
        return UpdateQuizEntity
    
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