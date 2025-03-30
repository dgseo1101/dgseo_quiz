# -*- coding: utf-8 -*-

from core.infrastructure.di.container import CoreContainer

from server.infrastructure.repositories.user_repository import UserRepository
from server.infrastructure.repositories.question_repository import QuestionRepository
from server.infrastructure.repositories.quiz_repository import QuizRepository
from server.infrastructure.repositories.choice_repository import ChoiceRepository
from server.infrastructure.repositories.quiz_attempt_repository import QuizAttemptRepository
from server.infrastructure.repositories.quiz_attempt_question_repository import QuizAttemptQuestionRepository
from server.infrastructure.repositories.attempt_seed_repository import AttemptSeedRepository
from server.infrastructure.repositories.session_repository import SessionRepository

# ======================================================================================

from server.application.services.user_service import UserService
from server.application.services.question_service import QuestionService
from server.application.services.quiz_service import QuizService
from server.application.services.choice_service import ChoiceService
from server.application.services.quiz_attempt_service import QuizAttemptService
from server.application.services.quiz_attempt_question_service import QuizAttemptQuestionService
from server.application.services.attempt_seed_service import AttemptSeedService


from dependency_injector import providers

class ServerContainer(CoreContainer):

    user_repository = providers.Singleton(
        UserRepository,
        session=CoreContainer.database.provided.session,
    )

    session_repository = providers.Singleton(
        SessionRepository,
        session=CoreContainer.database.provided.session,
    )

    question_repository = providers.Singleton(
        QuestionRepository,
        session=CoreContainer.database.provided.session,
    )

    quiz_repository = providers.Singleton(
        QuizRepository,
        session=CoreContainer.database.provided.session,
    )

    choice_repository = providers.Singleton(
        ChoiceRepository,
        session=CoreContainer.database.provided.session,
    )

    quiz_attempt_repository = providers.Singleton(
        QuizAttemptRepository,
        session=CoreContainer.database.provided.session,
    )

    quiz_attempt_question_repository = providers.Singleton(
        QuizAttemptQuestionRepository,
        session=CoreContainer.database.provided.session,
    )

    attempt_seed_repository = providers.Singleton(
        AttemptSeedRepository,
        session=CoreContainer.database.provided.session,
    )

    # ======================================================================================

    user_service = providers.Factory(
        UserService,
        user_repository=user_repository,
        session_repository=session_repository,
        config=CoreContainer.config
    )

    question_service = providers.Factory(
        QuestionService,
        question_repository=question_repository
    )

    quiz_service = providers.Factory(
        QuizService,
        quiz_repository=quiz_repository
    )

    choice_service = providers.Factory(
        ChoiceService,
        choice_repository=choice_repository
    )

    quiz_attempt_service = providers.Factory(
        QuizAttemptService,
        quiz_attempt_repository=quiz_attempt_repository,
        quiz_repository=quiz_repository,
        quiz_attempt_question_repository=quiz_attempt_question_repository,
        attempt_seed_repository=attempt_seed_repository
    )

    quiz_attempt_question_service = providers.Factory(
        QuizAttemptQuestionService,
        quiz_attempt_question_repository=quiz_attempt_question_repository
    )

    attempt_seed_service = providers.Factory(
        AttemptSeedService,
        attempt_seed_repository=attempt_seed_repository
    )



