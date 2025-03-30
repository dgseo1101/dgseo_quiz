from dependency_injector.wiring import Provide, inject
from typing import List
from fastapi import APIRouter, Depends, Request

from core.application.dtos.user_dto import (
    CreateUserRequestDto,
    UpdateUserRequestDto,
    UserResponseDto
)

from server.application.services.user_service import UserService
from server.infrastructure.di.container import ServerContainer

from server.application.dtos.auth_dto import (
    ResponseTokenDto,
    RefreshTokenRequestDto,
    AccessTokenResponseDto,
    LoginRequestDto
)

from server.shard_kernel.auth_helper import validate_user_and_get_user_id

router = APIRouter(prefix="/user", tags=["user"])

@router.post("/signup", summary="회원가입")
@inject
async def signup(
    create_data: CreateUserRequestDto,
    user_service: UserService = Depends(Provide[ServerContainer.user_service]),
) -> UserResponseDto:
    return await user_service.signup(create_data=create_data)

@router.post("/login", summary="로그인")
@inject
async def login(
    login_data: LoginRequestDto,
    user_service: UserService = Depends(Provide[ServerContainer.user_service]),
) -> ResponseTokenDto:
    return await user_service.login(login_data=login_data)

@router.post("/refresh", summary="refresh token")
@inject
async def refresh(
    refresh_token: RefreshTokenRequestDto,
    user_service: UserService = Depends(Provide[ServerContainer.user_service]),
) -> AccessTokenResponseDto:
    return await user_service.refresh(refresh_token=refresh_token)

@router.post("/logout", summary="로그아웃")
@inject
async def logout(
    user_id: int = Depends(validate_user_and_get_user_id),
    user_service: UserService = Depends(Provide[ServerContainer.user_service]),
) -> int:
    return await user_service.logout(user_id=user_id)