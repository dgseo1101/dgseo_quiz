# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy import DateTime, Integer, String, func, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column

from core.infrastructure.database.database import Base


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
