FROM python:3.11-slim

ENV POETRY_VIRTUALENVS_IN_PROJECT=true

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["bash", "-c", "./run.sh"]
