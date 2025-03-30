from dependency_injector.wiring import Provide, inject
from typing import List
from fastapi import APIRouter, Depends, Request

from core.application.dtos.choice_dto import (
    CreateChoiceRequestDto,
    UpdateChoiceRequestDto,
    ChoiceResponseDto
)

from server.application.services.choice_service import ChoiceService
from server.infrastructure.di.container import ServerContainer

from server.shard_kernel.auth_helper import validate_admin_and_get_user_id

router = APIRouter(prefix="/choice", tags=["choice"])


@router.post("")
@inject
async def create_choice(
    create_data: CreateChoiceRequestDto,
    user_id: int = Depends(validate_admin_and_get_user_id),
    choice_service: ChoiceService = Depends(Provide[ServerContainer.choice_service])
)->ChoiceResponseDto:
    return await choice_service.create_data(create_data=create_data)

@router.put("/{choice_id}")
@inject
async def update_choice(
    choice_id: int,
    update_data: UpdateChoiceRequestDto,
    user_id: int = Depends(validate_admin_and_get_user_id),
    choice_service: ChoiceService = Depends(Provide[ServerContainer.choice_service])
)->ChoiceResponseDto:
    return await choice_service.update_data_by_data_id(data_id=choice_id, update_data=update_data)

@router.delete("/{choice_id}")
@inject
async def delete_choice(
    choice_id: int,
    user_id: int = Depends(validate_admin_and_get_user_id),
    choice_service: ChoiceService = Depends(Provide[ServerContainer.choice_service])
)->int:
    await choice_service.delete_data_by_data_id(data_id=choice_id)
    return 200