FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install pipenv

RUN pipenv install --system --deploy

CMD ["python", "src/main.py"]