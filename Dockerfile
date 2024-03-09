FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install "poetry==1.7.0"

RUN poetry config virtualenvs.create false
RUN poetry config installer.max-workers 1
RUN poetry install --without dev,test --no-interaction --no-ansi

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
