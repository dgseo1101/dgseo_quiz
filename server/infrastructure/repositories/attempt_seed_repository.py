from contextlib import AbstractAsyncContextManager
from typing import Callable

from sqlalchemy.ext.asyncio import AsyncSession

from core.infrastructure.database.models.attempt_seed_model import AttempSeedModel
from core.infrastructure.repositories.base_repository import BaseRepository

from core.domain.entities.attempt_seed_entity import (
    AttemptSeedEntity,
    CreateAttemptSeedEntity,
    UpdateAttemptSeedEntity,
)

SessionFactory = Callable[..., AbstractAsyncContextManager[AsyncSession]]


class AttemptSeedRepository(BaseRepository):
    def __init__(self, session: SessionFactory) -> None:
        self.session = session

    @property
    def model(self):
        return AttempSeedModel 

    @property
    def create_entity(self):
        return CreateAttemptSeedEntity

    @property
    def return_entity(self):
        return AttemptSeedEntity

    @property
    def update_entity(self):
        return UpdateAttemptSeedEntity