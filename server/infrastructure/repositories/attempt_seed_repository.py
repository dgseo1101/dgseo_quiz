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
        return AttempSeedModel  # 유저 엔티티를 반환

    @property
    def create_entity(self):
        # 여기에서 필요한 로직으로 엔티티를 생성할 수 있음
        return CreateAttemptSeedEntity

    @property
    def return_entity(self):
        # 반환할 때 사용하는 DTO 또는 엔티티 정의
        return AttemptSeedEntity

    @property
    def update_entity(self):
        # 업데이트 시 사용하는 엔티티나 로직
        return UpdateAttemptSeedEntity