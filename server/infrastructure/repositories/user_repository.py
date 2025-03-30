from contextlib import AbstractAsyncContextManager
from typing import Callable

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.infrastructure.database.models.user_model import UserModel
from core.infrastructure.repositories.base_repository import BaseRepository

from core.application.dtos.user_dto import UserResponseDto
from server.application.dtos.auth_dto import LoginRequestDto

from core.domain.entities.user_entity import (
    UserEntity,
    CreateUserEntity,
    UpdateUserEntity,
)

SessionFactory = Callable[..., AbstractAsyncContextManager[AsyncSession]]


class UserRepository(BaseRepository):
    def __init__(self, session: SessionFactory) -> None:
        self.session = session

    @property
    def model(self):
        return UserModel

    @property
    def create_entity(self):
        return CreateUserEntity

    @property
    def return_entity(self):
        return UserEntity

    @property
    def update_entity(self):
        return UpdateUserEntity
    
    async def exists_user_by_email(self, login_data: LoginRequestDto):
        async with self.session() as session:
            stmt = select(UserModel).where(UserModel.email == login_data.email)
            result = await session.execute(stmt)
            data = result.scalars().first()

            if data:
                return UserResponseDto(**vars(data))
            
        return None
    
    async def get_data_by_email(self, email: str):
        async with self.session() as session:
            result = await session.execute(
                select(UserModel).where(UserModel.email == email)
            )
            data = result.scalars().first()
        
        return UserResponseDto(**vars(data))