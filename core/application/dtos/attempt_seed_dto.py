from datetime import datetime
from typing import Optional

from core.application.dtos.base import BaseRequest, BaseResponse

class CreateAttemptSeedRequestDto(BaseRequest):
    quiz_attempt_id: int
    seed: int

class UpdateAttemptSeedRequestDto(BaseRequest):
    quiz_attempt_id: int
    seed: int

class AttemptSeedResponseDto(BaseResponse):
    id: int
    quiz_attempt_id: int
    seed: int