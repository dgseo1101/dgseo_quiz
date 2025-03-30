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

router = APIRouter(prefix="/assignment", tags=["응시자 관리"])

@router.get("")
@inject
async def get_assignments(
    page: int = 1,
    page_size: int = 10,
    assignment_service: AssignmentService = Depends(Provide[ServerContainer.assignment_service])
)->List[AssignmentResponseDto]:
    return await assignment_service.get_datas(page=page, page_size=page_size)

@router.get("/{assignment_id}")
@inject
async def get_assignment(
    assignment_id: int,
    assignment_service: AssignmentService = Depends(Provide[ServerContainer.assignment_service])
)->AssignmentResponseDto:
    return await assignment_service.get_data_by_data_id(data_id=assignment_id)

@router.post("")
@inject
async def create_assignment(
    create_data: CreateAssignmentRequestDto,
    assignment_service: AssignmentService = Depends(Provide[ServerContainer.assignment_service])
)->AssignmentResponseDto:
    return await assignment_service.create_data(create_data=create_data)

@router.put("/{assignment_id}")
@inject
async def update_assignment(
    assignment_id: int,
    update_data: UpdateAssignmenRequestDto,
    assignment_service: AssignmentService = Depends(Provide[ServerContainer.assignment_service])
)->AssignmentResponseDto:
    return await assignment_service.update_data_by_data_id(data_id=assignment_id, update_data=update_data)

@router.delete("/{assignment_id}")
@inject
async def delete_assignment(
    assignment_id: int,
    assignment_service: AssignmentService = Depends(Provide[ServerContainer.assignment_service])
)->int:
    await assignment_service.delete_data_by_data_id(data_id=assignment_id)
    return 200