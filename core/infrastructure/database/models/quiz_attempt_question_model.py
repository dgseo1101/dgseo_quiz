# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy import DateTime, Integer, func, ForeignKey, Text, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.infrastructure.database.database import Base

# 유저가 출제받은 문제를 저장하는 테이블
class QuizAttemptQuestionModel(Base):
    __tablename__ = "quiz_attempt_question"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    quiz_attempt_id: Mapped[int] = mapped_column(ForeignKey("quiz_attempt.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    question_id: Mapped[int] = mapped_column(ForeignKey("question.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    question_order: Mapped[int] = mapped_column(Integer, nullable=False)
    selected_choice_id: Mapped[int] = mapped_column(ForeignKey("choice.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=True)
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        server_onupdate=func.now(),
    )

    attempt = relationship("QuizAttemptModel", back_populates="attempt_questions")
    question = relationship("QuestionModel")
    selected_choice = relationship("ChoiceModel")
