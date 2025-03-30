# -*- coding: utf-8 -*-
import logging

from core.application.dtos.attempt_seed_dto import (
    CreateAttemptSeedRequestDto,
    AttemptSeedResponseDto,
    UpdateAttemptSeedRequestDto,
)
from core.application.services.base_service import BaseService
from server.infrastructure.repositories.attempt_seed_repository import AttemptSeedRepository


class AttemptSeedService(BaseService):
    def __init__(self, attempt_seed_repository: AttemptSeedRepository) -> None:
        super().__init__(base_repository=attempt_seed_repository)
        self.logger = logging.getLogger(__name__)
        self.attempt_seed_repository = attempt_seed_repository

    @property
    def create_dto(self):
        return CreateAttemptSeedRequestDto

    @property
    def response_dto(self):
        return AttemptSeedResponseDto

    @property
    def update_dto(self):
        return UpdateAttemptSeedRequestDto
