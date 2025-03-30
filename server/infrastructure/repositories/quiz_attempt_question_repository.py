from contextlib import AbstractAsyncContextManager
from typing import Callable

from sqlalchemy.ext.asyncio import AsyncSession

from core.infrastructure.database.models.quiz_attempt_question_model import QuizAttemptQuestionModel
from core.infrastructure.repositories.base_repository import BaseRepository

from core.domain.entities.quiz_attempt_question_entity import (
    QuizAttemptQuestionEntity,
    CreateQuizAttemptQuestionEntity,
    UpdateQuizAttemptQuestionEntity,
)

SessionFactory = Callable[..., AbstractAsyncContextManager[AsyncSession]]


class QuizAttemptQuestionRepository(BaseRepository):
    def __init__(self, session: SessionFactory) -> None:
        self.session = session

    @property
    def model(self):
        return QuizAttemptQuestionModel  # 유저 엔티티를 반환

    @property
    def create_entity(self):
        # 여기에서 필요한 로직으로 엔티티를 생성할 수 있음
        return CreateQuizAttemptQuestionEntity

    @property
    def return_entity(self):
        # 반환할 때 사용하는 DTO 또는 엔티티 정의
        return QuizAttemptQuestionEntity

    @property
    def update_entity(self):
        # 업데이트 시 사용하는 엔티티나 로직
        return UpdateQuizAttemptQuestionEntity