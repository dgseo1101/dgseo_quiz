# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy import DateTime, Integer, func, ForeignKey, Text, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from core.infrastructure.database.database import Base


# 시험 응시 테이블
class QuizAttemptModel(Base):
    __tablename__ = "quiz_attempt"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    quiz_id: Mapped[int] = mapped_column(ForeignKey("quiz.id"), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        server_onupdate=func.now(),
    )
