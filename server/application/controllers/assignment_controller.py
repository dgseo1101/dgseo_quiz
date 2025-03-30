from dependency_injector.wiring import Provide, inject
from typing import List
from fastapi import APIRouter, Depends, Request

from core.application.dtos.assignment_dto import (
    CreateAssignmentRequestDto,
    UpdateAssignmenRequestDto,
    AssignmentResponseDto
)

from server.application.services.assignment_service import AssignmentService
from server.infrastructure.di.container import ServerContainer

from server.shard_kernel.auth_helper import validate_admin_and_get_user_id


router = APIRouter(prefix="/assignment", tags=["응시자 관리"])

@router.get("")
@inject
async def get_assignments(
    page: int = 1,
    page_size: int = 10,
    user_id: int = Depends(validate_admin_and_get_user_id),
    assignment_service: AssignmentService = Depends(Provide[ServerContainer.assignment_service])
)->List[AssignmentResponseDto]:
    return await assignment_service.get_datas(page=page, page_size=page_size)

@router.post("")
@inject
async def create_assignment(
    create_data: CreateAssignmentRequestDto,
    user_id: int = Depends(validate_admin_and_get_user_id),
    assignment_service: AssignmentService = Depends(Provide[ServerContainer.assignment_service])
)->AssignmentResponseDto:
    return await assignment_service.create_data(create_data=create_data)

@router.put("/{assignment_id}")
@inject
async def update_assignment(
    assignment_id: int,
    update_data: UpdateAssignmenRequestDto,
    user_id: int = Depends(validate_admin_and_get_user_id),
    assignment_service: AssignmentService = Depends(Provide[ServerContainer.assignment_service])
)->AssignmentResponseDto:
    return await assignment_service.update_data_by_data_id(data_id=assignment_id, update_data=update_data)

@router.delete("/{assignment_id}")
@inject
async def delete_assignment(
    assignment_id: int,
    user_id: int = Depends(validate_admin_and_get_user_id),
    assignment_service: AssignmentService = Depends(Provide[ServerContainer.assignment_service])
)->int:
    await assignment_service.delete_data_by_data_id(data_id=assignment_id)
    return 200