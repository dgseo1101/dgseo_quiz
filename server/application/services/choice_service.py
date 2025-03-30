# -*- coding: utf-8 -*-
import logging

from core.application.dtos.choice_dto import (
    CreateChoiceRequestDto,
    ChoiceResponseDto,
    UpdateChoiceRequestDto,
)
from core.application.services.base_service import BaseService
from server.infrastructure.repositories.choice_repository import ChoiceRepository


class ChoiceService(BaseService):
    def __init__(self, choice_repository: ChoiceRepository) -> None:
        super().__init__(base_repository=choice_repository)
        self.logger = logging.getLogger(__name__)
        self.choice_repository = choice_repository

    @property
    def create_dto(self):
        return CreateChoiceRequestDto

    @property
    def response_dto(self):
        return ChoiceResponseDto

    @property
    def update_dto(self):
        return UpdateChoiceRequestDto
