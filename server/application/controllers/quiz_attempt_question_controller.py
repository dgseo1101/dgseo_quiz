from dependency_injector.wiring import Provide, inject
from typing import List
from fastapi import APIRouter, Depends, Request

from core.application.dtos.quiz_attempt_question_dto import (
    CreateQuizAttemptQuestionRequestDto,
    UpdateQuizAttemptQuestionRequestDto,
    QuizAttemptQuestionResponseDto
)

from server.application.services.quiz_attempt_question_service import QuizAttemptQuestionService
from server.infrastructure.di.container import ServerContainer

router = APIRouter(prefix="/quiz_attempt_question", tags=["quiz_attempt_question"])

@router.get("")
@inject
async def get_quiz_attempt_questions(
    page: int = 1,
    page_size: int = 10,
    quiz_attempt_question_service: QuizAttemptQuestionService = Depends(Provide[ServerContainer.quiz_attempt_question_service])
)->List[QuizAttemptQuestionResponseDto]:
    return await quiz_attempt_question_service.get_datas(page=page, page_size=page_size)

@router.get("/{quiz_attempt_question_id}")
@inject
async def get_quiz_attempt_question(
    quiz_attempt_question_id: int,
    quiz_attempt_question_service: QuizAttemptQuestionService = Depends(Provide[ServerContainer.quiz_attempt_question_service])
)->QuizAttemptQuestionResponseDto:
    return await quiz_attempt_question_service.get_data_by_data_id(data_id=quiz_attempt_question_id)

@router.post("")
@inject
async def create_quiz_attempt_question(
    create_data: CreateQuizAttemptQuestionRequestDto,
    quiz_attempt_question_service: QuizAttemptQuestionService = Depends(Provide[ServerContainer.quiz_attempt_question_service])
)->QuizAttemptQuestionResponseDto:
    return await quiz_attempt_question_service.create_data(create_data=create_data)

@router.put("/{quiz_attempt_question_id}")
@inject
async def update_quiz_attempt_question(
    quiz_attempt_question_id: int,
    update_data: UpdateQuizAttemptQuestionRequestDto,
    quiz_attempt_question_service: QuizAttemptQuestionService = Depends(Provide[ServerContainer.quiz_attempt_question_service])
)->QuizAttemptQuestionResponseDto:
    return await quiz_attempt_question_service.update_data_by_data_id(data_id=quiz_attempt_question_id, update_data=update_data)

@router.delete("/{quiz_attempt_question_id}")
@inject
async def delete_quiz_attempt_question(
    quiz_attempt_question_id: int,
    quiz_attempt_question_service: QuizAttemptQuestionService = Depends(Provide[ServerContainer.quiz_attempt_question_service])
)->int:
    await quiz_attempt_question_service.delete_data_by_data_id(data_id=quiz_attempt_question_id)
    return 200