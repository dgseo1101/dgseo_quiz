# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy import DateTime, Integer, func, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.infrastructure.database.database import Base

# 퀴즈에 포함된 문제 테이블
class QuestionModel(Base):
    __tablename__ = "question"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    quiz_id: Mapped[int] = mapped_column(ForeignKey("quiz.id"), nullable=False)
    content: Mapped[str] = mapped_column(Text, default="", nullable=False)
    display_order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        server_onupdate=func.now(),
    )

    quiz = relationship("QuizModel", back_populates="questions")
    choices = relationship("ChoiceModel", back_populates="question", cascade="all, delete-orphan")
