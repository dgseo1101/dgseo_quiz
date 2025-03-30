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
        return QuizAttemptQuestionModel 

    @property
    def create_entity(self):
        return CreateQuizAttemptQuestionEntity

    @property
    def return_entity(self):
        return QuizAttemptQuestionEntity

    @property
    def update_entity(self):
        return UpdateQuizAttemptQuestionEntity