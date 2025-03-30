# -*- coding: utf-8 -*-
from contextlib import AbstractAsyncContextManager
from typing import Callable

from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import exists

from core.infrastructure.database.models.session_model import SessionsModel
from core.infrastructure.repositories.base_repository import BaseRepository
from core.domain.entities.session_entity import (
    UserSessionResponseEntity,
    CreateUserSessionRequestEntity,
)

SessionFactory = Callable[..., AbstractAsyncContextManager[AsyncSession]]


class SessionRepository(BaseRepository):
    def __init__(self, session: SessionFactory) -> None:
        self.session = session

    @property
    def model(self):
        return SessionsModel

    @property
    def create_entity(self):
        return CreateUserSessionRequestEntity

    @property
    def return_entity(self):
        return UserSessionResponseEntity
    
    @property
    def update_entity(self):
        pass

    async def exists_refresh_token(self, refresh_token: str):
        async with self.session() as session:
            stmt = select(
                exists().where(SessionsModel.token == refresh_token)
            )
            result = await session.execute(stmt)
            exists_result = result.scalars().first()

        return exists_result
    
    async def delete_data_by_user_id(self, user_id: int):
        async with self.session() as session:
            stmt = delete(SessionsModel).where(SessionsModel.user_id == user_id)
            await session.execute(stmt)
            await session.commit()