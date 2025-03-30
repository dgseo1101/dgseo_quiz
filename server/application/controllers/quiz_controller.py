from dependency_injector.wiring import Provide, inject
from typing import List, Optional
from fastapi import APIRouter, Depends, Request

from core.application.dtos.quiz_dto import (
    UpdateQuizRequestDto,
    QuizResponseDto
)

from server.application.services.quiz_service import QuizService
from server.infrastructure.di.container import ServerContainer

from server.shard_kernel.auth_helper import (
    validate_user_and_get_user_id,
    validate_admin_and_get_user_id
)

from server.application.dtos.quiz_dto import (
    QuizCreate,
    QuizDetailResponseDto
)

router = APIRouter(prefix="/quiz", tags=["quiz"])

@router.get("", summary="전체 시험 조회")
@inject
async def get_quizs(
    page: int = 1,
    page_size: int = 10,
    user_id: int = Depends(validate_admin_and_get_user_id),
    quiz_service: QuizService = Depends(Provide[ServerContainer.quiz_service])
)->List[QuizResponseDto]:
    return await quiz_service.get_datas(page=page, page_size=page_size)

@router.get("/assigned-quiz", summary="유저가 응시할 시험 조회")
@inject
async def get_quiz_by_user(
    page: int = 1,
    page_size: int = 10,
    user_id: int = Depends(validate_user_and_get_user_id),
    quiz_service: QuizService = Depends(Provide[ServerContainer.quiz_service])
)->List[QuizResponseDto]:
    return await quiz_service.get_data_by_user_id(user_id=user_id, page=page, page_size=page_size)

@router.get("/{quiz_id}", summary="시험 조회")
@inject
async def get_quiz(
    quiz_id: int,
    seed: Optional[int] = None, #시드가 없을 시, 최초로 설정하여 리턴, 이후부턴 동일한 시드 입력
    page: int = 1,
    user_id: int = Depends(validate_user_and_get_user_id),
    quiz_service: QuizService = Depends(Provide[ServerContainer.quiz_service])
)->QuizDetailResponseDto:
    return await quiz_service.get_quiz(quiz_id=quiz_id, page=page, seed=seed)

@router.post("", summary="시험 생성")
@inject
async def create_quiz(
    create_data: QuizCreate,
    user_id: int = Depends(validate_admin_and_get_user_id),
    quiz_service: QuizService = Depends(Provide[ServerContainer.quiz_service])
)->QuizResponseDto:
    return await quiz_service.create_quiz(create_data=create_data, user_id=user_id)

@router.put("/{quiz_id}", summary="시험 업데이트")
@inject
async def update_quiz(
    quiz_id: int,
    update_data: UpdateQuizRequestDto,
    user_id: int = Depends(validate_admin_and_get_user_id),
    quiz_service: QuizService = Depends(Provide[ServerContainer.quiz_service])
)->QuizResponseDto:
    return await quiz_service.update_data_by_data_id(data_id=quiz_id, update_data=update_data)

@router.delete("/{quiz_id}", summary="시험 삭제")
@inject
async def delete_quiz(
    quiz_id: int,
    user_id: int = Depends(validate_admin_and_get_user_id),
    quiz_service: QuizService = Depends(Provide[ServerContainer.quiz_service])
)->int:
    await quiz_service.delete_data_by_data_id(data_id=quiz_id)
    return 200