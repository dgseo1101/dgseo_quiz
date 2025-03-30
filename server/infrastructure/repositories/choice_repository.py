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
        return ChoiceModel  # 유저 엔티티를 반환

    @property
    def create_entity(self):
        # 여기에서 필요한 로직으로 엔티티를 생성할 수 있음
        return CreateChoiceEntity

    @property
    def return_entity(self):
        # 반환할 때 사용하는 DTO 또는 엔티티 정의
        return ChoiceEntity

    @property
    def update_entity(self):
        # 업데이트 시 사용하는 엔티티나 로직
        return UpdateChoiceEntity