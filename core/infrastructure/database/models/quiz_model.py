# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy import DateTime, Integer, String, func, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.infrastructure.database.database import Base


# 퀴즈 (시험지) 테이블
class QuizModel(Base):
    __tablename__ = "quiz"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255), default="", nullable=False)
    description: Mapped[str] = mapped_column(String(255), default="", nullable=False)
    created_by: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        server_onupdate=func.now(),
    )

    randomize_questions: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    randomize_choices:Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    num_questions_to_display:Mapped[bool] = mapped_column(Integer, nullable=False)

    creator = relationship("UserModel", back_populates="quiz")
    questions = relationship("QuestionModel", back_populates="quiz", cascade="all, delete-orphan")
    attempts = relationship("QuizAttemptModel", back_populates="quiz")