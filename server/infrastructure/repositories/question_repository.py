from contextlib import AbstractAsyncContextManager
from typing import Callable

from sqlalchemy.ext.asyncio import AsyncSession

from core.infrastructure.database.models.question_model import QuestionModel
from core.infrastructure.database.models.choice_model import ChoiceModel
from core.infrastructure.repositories.base_repository import BaseRepository

from core.domain.entities.question_entity import (
    QuestionEntity,
    CreateQuestionEntity,
    UpdateQuestionEntity,
)

from server.application.dtos.quiz_dto import QuestionCreate

SessionFactory = Callable[..., AbstractAsyncContextManager[AsyncSession]]


class QuestionRepository(BaseRepository):
    def __init__(self, session: SessionFactory) -> None:
        self.session = session

    @property
    def model(self):
        return QuestionModel 

    @property
    def create_entity(self):
        return CreateQuestionEntity

    @property
    def return_entity(self):
        return QuestionEntity

    @property
    def update_entity(self):
        return UpdateQuestionEntity