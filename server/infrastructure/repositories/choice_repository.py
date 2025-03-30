from contextlib import AbstractAsyncContextManager
from typing import Callable

from sqlalchemy.ext.asyncio import AsyncSession

from core.infrastructure.database.models.choice_model import ChoiceModel
from core.infrastructure.repositories.base_repository import BaseRepository

from core.domain.entities.choice_entity import (
    CreateChoiceEntity,
    ChoiceEntity,
    UpdateChoiceEntity,
)

SessionFactory = Callable[..., AbstractAsyncContextManager[AsyncSession]]


class ChoiceRepository(BaseRepository):
    def __init__(self, session: SessionFactory) -> None:
        self.session = session

    @property
    def model(self):
        return ChoiceModel

    @property
    def create_entity(self):
        return CreateChoiceEntity

    @property
    def return_entity(self):
        return ChoiceEntity

    @property
    def update_entity(self):
        return UpdateChoiceEntity