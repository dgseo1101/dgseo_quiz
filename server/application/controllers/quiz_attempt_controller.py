from dependency_injector.wiring import Provide, inject
from typing import List
from fastapi import APIRouter, Depends, Request

from server.application.services.quiz_attempt_service import QuizAttemptService
from server.infrastructure.di.container import ServerContainer

from server.application.dtos.quiz_attempt_dto import (
    QuizSubmitRequestDto,
    QuizAttemptWithSeedResponseDto
)

from server.shard_kernel.auth_helper import validate_user_and_get_user_id

router = APIRouter(prefix="/quiz_attempt", tags=["quiz_attempt"])

@router.get("", summary="유저가 응시중인/응시한 시험 정보")
@inject
async def get_quiz_attempt(
    user_id: int = Depends(validate_user_and_get_user_id),
    quiz_attempt_service: QuizAttemptService = Depends(Provide[ServerContainer.quiz_attempt_service])
)-> List[QuizAttemptWithSeedResponseDto]:
    return await quiz_attempt_service.get_quiz_attempt(user_id=user_id)

@router.post("/{quiz_id}/start", summary="시험 응시시 자동으로 호출되는 api")
@inject
async def start_quiz(
    quiz_id: int,
    seed: int,
    user_id: int = Depends(validate_user_and_get_user_id),
    quiz_attempt_service: QuizAttemptService = Depends(Provide[ServerContainer.quiz_attempt_service])
):
    return await quiz_attempt_service.start_quiz_attempt(quiz_id=quiz_id, user_id=user_id, seed=seed)

@router.post("/{attempt_id}/submit", summary="시험 제출")
@inject
async def submit_quiz(
    attempt_id: int,
    submission: QuizSubmitRequestDto,
    user_id: int = Depends(validate_user_and_get_user_id),
    quiz_attempt_service: QuizAttemptService = Depends(Provide[ServerContainer.quiz_attempt_service])
):
    return await quiz_attempt_service.submit_quiz_attempt(attempt_id=attempt_id, submission=submission)