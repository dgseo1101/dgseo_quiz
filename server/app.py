# -*- coding: utf-8 -*-
from fastapi import FastAPI

from server.infrastructure.di.container import ServerContainer
from server.application.controllers.user_controller import router as user_router
from server.application.controllers.choice_controller import router as choice_router
from server.application.controllers.question_controller import router as question_router
from server.application.controllers.quiz_controller import router as quiz_router
from server.application.controllers.quiz_attempt_controller import router as quiz_attempt_router
from server.application.controllers.quiz_attempt_question_controller import router as quiz_attempt_question_router
from server.application.controllers.attempt_seed_controller import router as attempt_seed_router

container = None


def create_container():
    container = ServerContainer()
    container.wire(packages=["server.application.controllers"])

    container.config.from_yaml("./config.yml")

    return container


def create_app():
    global container
    container = create_container()

    app = FastAPI(docs_url="/docs")
    app.include_router(router=user_router)
    app.include_router(router=quiz_router)
    app.include_router(router=question_router)
    app.include_router(router=quiz_attempt_router)

    return app


app = create_app()
