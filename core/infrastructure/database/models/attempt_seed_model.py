# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy import DateTime, Integer, func, ForeignKey, Text, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.infrastructure.database.database import Base

# 관리자가 선택지의 랜덤 배치를 설정한 경우,  각 응시 문제별로 실제 랜덤 배치된 선택지의 순서를 별도로 저장
class AttempSeed(Base):
    __tablename__ = "attempt_seed"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    quiz_attempt_id: Mapped[int] = mapped_column(ForeignKey("quiz_attempt.id"), nullable=False)
    seed: Mapped[int] = mapped_column(Integer, nullable=False)
