from datetime import datetime
from typing import Optional

from core.application.dtos.base import BaseRequest, BaseResponse

class CreateAssignmentRequestDto(BaseRequest):
    user_id: int
    quiz_id: int

class UpdateAssignmenRequestDto(BaseRequest):
    user_id: Optional[int] = None
    quiz_id: Optional[int] = None

class AssignmentResponseDto(BaseResponse):
    id: int
    user_id: int
    quiz_id: int
    created_at: datetime
    updated_at: datetime