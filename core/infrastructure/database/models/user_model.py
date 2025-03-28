# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy import DateTime, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column

from core.infrastructure.database.database import Base

from core.domain.enums.user_enums import UserRole


class UsersModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), default="", nullable=False)
    email: Mapped[str] = mapped_column(String(255), default="", nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), default="", nullable=False)
    role: Mapped[str] = mapped_column(UserRole, default=UserRole.USER.value(), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        server_onupdate=func.now(),
    )
