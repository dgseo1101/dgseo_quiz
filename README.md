1. **프로젝트 설치**
    ```bash
    git clone https://github.com/dgseo1101/dgseo_quiz.git
    cd dgseo_quiz
    ```

2. **의존성 설치 및 env 설정**
    ```bash
    pip install poetry
    poetry shell
    poetry install

    mkdir _env
    vi _env/dev.
    
    ###
    SERVICE_NAME=global

    DATABASE_USER=your_mysql_user_name
    DATABASE_PASSWORD=your_mysql_password
    DATABASE_HOST=your_mysql_host
    DATABASE_PORT=your_mysql_port
    DATABASE_NAME=your_mysql_db_name

    JWT_SECRET_KEY=global
    JWT_ALGORITHM=HS256
    ```

3. **데이터베이스 마이그레이션**
    ```bash
    (poetry-shell) alembic revision --autogenerate -m "init"
    (poetry-shell) alembic upgrade head
    ```


4. **서버 실행**
    ```
    (poetry-shell) python run_server_local.py
    ```
