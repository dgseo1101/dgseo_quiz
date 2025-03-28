# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy import DateTime, Integer, func, ForeignKey, Text, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from core.infrastructure.database.database import Base


# 시험 응시 테이블
class QuizAttemptQuestionModel(Base):
    __tablename__ = "quiz_attempt_question"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    attempt_id: Mapped[int] = mapped_column(ForeignKey("attempt.id"), nullable=False)
    question_id: Mapped[int] = mapped_column(ForeignKey("question.id"), nullable=False)
    question_order: Mapped[int] = mapped_column(Integer, nullable=False)
    selected_choice_id: Mapped[int] = mapped_column(ForeignKey("choice.id"), nullable=True)
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        server_onupdate=func.now(),
    )
