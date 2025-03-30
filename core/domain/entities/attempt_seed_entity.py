from datetime import datetime
from typing import Optional

from core.domain.entities.entity import Entity

class CreateAttemptSeedEntity(Entity):
    quiz_attempt_id: int
    seed: int

class UpdateAttemptSeedEntity(Entity):
    quiz_attempt_id: int
    seed: int

class AttemptSeedEntity(Entity):
    id: int
    quiz_attempt_id: int
    seed: int