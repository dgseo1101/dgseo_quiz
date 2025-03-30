# -*- coding: utf-8 -*-
import logging

from core.application.dtos.assignment_dto import (
    CreateAssignmentRequestDto,
    AssignmentResponseDto,
    UpdateAssignmenRequestDto,
)
from core.application.services.base_service import BaseService
from server.infrastructure.repositories.assignment_repository import AssignmentRepository


class AssignmentService(BaseService):
    def __init__(self, assignment_repository: AssignmentRepository) -> None:
        super().__init__(base_repository=assignment_repository)
        self.logger = logging.getLogger(__name__)
        self.assignment_repository = assignment_repository

    @property
    def create_dto(self):
        return CreateAssignmentRequestDto

    @property
    def response_dto(self):
        return AssignmentResponseDto

    @property
    def update_dto(self):
        return UpdateAssignmenRequestDto
