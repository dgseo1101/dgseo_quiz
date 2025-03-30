from dependency_injector.wiring import Provide, inject
from typing import List
from fastapi import APIRouter, Depends, Request

from core.application.dtos.attempt_seed_dto import (
    CreateAttemptSeedRequestDto,
    UpdateAttemptSeedRequestDto,
    AttemptSeedResponseDto
)

from server.application.services.attempt_seed_service import AttemptSeedService
from server.infrastructure.di.container import ServerContainer

router = APIRouter(prefix="/attempt_seed", tags=["attempt_seed"])

@router.get("")
@inject
async def get_attempt_seeds(
    page: int = 1,
    page_size: int = 10,
    attempt_seed_service: AttemptSeedService = Depends(Provide[ServerContainer.attempt_seed_service])
)->List[AttemptSeedResponseDto]:
    return await attempt_seed_service.get_datas(page=page, page_size=page_size)

@router.get("/{attempt_seed_id}")
@inject
async def get_attempt_seed(
    attempt_seed_id: int,
    attempt_seed_service: AttemptSeedService = Depends(Provide[ServerContainer.attempt_seed_service])
)->AttemptSeedResponseDto:
    return await attempt_seed_service.get_data_by_data_id(data_id=attempt_seed_id)

@router.post("")
@inject
async def create_attempt_seed(
    create_data: CreateAttemptSeedRequestDto,
    attempt_seed_service: AttemptSeedService = Depends(Provide[ServerContainer.attempt_seed_service])
)->AttemptSeedResponseDto:
    return await attempt_seed_service.create_data(create_data=create_data)

@router.put("/{attempt_seed_id}")
@inject
async def update_attempt_seed(
    attempt_seed_id: int,
    update_data: UpdateAttemptSeedRequestDto,
    attempt_seed_service: AttemptSeedService = Depends(Provide[ServerContainer.attempt_seed_service])
)->AttemptSeedResponseDto:
    return await attempt_seed_service.update_data_by_data_id(data_id=attempt_seed_id, update_data=update_data)

@router.delete("/{attempt_seed_id}")
@inject
async def delete_attempt_seed(
    attempt_seed_id: int,
    attempt_seed_service: AttemptSeedService = Depends(Provide[ServerContainer.attempt_seed_service])
)->int:
    await attempt_seed_service.delete_data_by_data_id(data_id=attempt_seed_id)
    return 200