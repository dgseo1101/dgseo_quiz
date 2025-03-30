# -*- coding: utf-8 -*-
# flake8: noqa: F401, F403

import os
from logging.config import fileConfig
from urllib.parse import quote_plus

from alembic import context
from dotenv import load_dotenv
from sqlalchemy import create_engine

from core.infrastructure.database.database import Base
from core.infrastructure.database.models.user_model import UserModel
from core.infrastructure.database.models.choice_model import ChoiceModel
from core.infrastructure.database.models.question_model import QuestionModel
from core.infrastructure.database.models.quiz_model import QuizModel
from core.infrastructure.database.models.quiz_attempt_model import QuizAttemptModel
from core.infrastructure.database.models.quiz_attempt_question_model import QuizAttemptQuestionModel
from core.infrastructure.database.models.attempt_seed_model import AttempSeed
from core.infrastructure.database.models.session_model import SessionsModel

load_dotenv(dotenv_path=f"_env/dev.env", override=True)

DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = quote_plus(os.getenv("DATABASE_PASSWORD"))
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_NAME = os.getenv("DATABASE_NAME")

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

url = f"postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"


def run_migrations_offline() -> None:
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = create_engine(
        url=url,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_schemas=False,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
