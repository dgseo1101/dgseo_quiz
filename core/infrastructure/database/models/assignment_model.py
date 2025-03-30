# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy import DateTime, Integer, func, ForeignKey, Text, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.infrastructure.database.database import Base

# 관리자가 유저가 응시할 시험을 관리하는 테이블
class AssignmentModel(Base):
    __tablename__ = "assignment"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    quiz_id: Mapped[int] = mapped_column(ForeignKey("quiz.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        server_onupdate=func.now(),
    )