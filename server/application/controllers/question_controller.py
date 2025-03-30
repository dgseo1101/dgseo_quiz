from dependency_injector.wiring import Provide, inject
from typing import List
from fastapi import APIRouter, Depends, Request

from core.application.dtos.question_dto import (
    UpdateQuestionRequestDto,
    QuestionResponseDto
)

from server.application.dtos.quiz_dto import (
    QuestionCreate
)

from server.application.services.question_service import QuestionService
from server.infrastructure.di.container import ServerContainer

from server.shard_kernel.auth_helper import validate_admin_and_get_user_id

router = APIRouter(prefix="/question", tags=["question"])

@router.post("/{quiz_id}", summary="시험 문제와 항목 생성")
@inject
async def create_question(
    create_data: QuestionCreate,
    quiz_id: int,
    user_id: int = Depends(validate_admin_and_get_user_id),
    question_service: QuestionService = Depends(Provide[ServerContainer.question_service])
)->QuestionResponseDto:
    return await question_service.create_question(quiz_id=quiz_id, create_data=create_data)

@router.put("/{question_id}", summary="시험 문제 업데이트")
@inject
async def update_question(
    question_id: int,
    update_data: UpdateQuestionRequestDto,
    user_id: int = Depends(validate_admin_and_get_user_id),
    question_service: QuestionService = Depends(Provide[ServerContainer.question_service])
)->QuestionResponseDto:
    return await question_service.update_data_by_data_id(data_id=question_id, update_data=update_data)

@router.delete("/{question_id}", summary="시험 문제 삭제")
@inject
async def delete_question(
    question_id: int,
    user_id: int = Depends(validate_admin_and_get_user_id),
    question_service: QuestionService = Depends(Provide[ServerContainer.question_service])
)->int:
    await question_service.delete_data_by_data_id(data_id=question_id)
    return 200