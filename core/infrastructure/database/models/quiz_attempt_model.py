# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy import DateTime, Integer, func, ForeignKey, Text, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.infrastructure.database.database import Base


# 시험 응시시 생성되는 세션 정보를 저장하는 테이블
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

    quiz = relationship("QuizModel", back_populates="attempts")
    user = relationship("UserModel", back_populates="attempts")
    attempt_questions = relationship("QuizAttemptQuestionModel", back_populates="attempt", cascade="all, delete-orphan")

