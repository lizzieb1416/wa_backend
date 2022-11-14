# syntax=docker/dockerfile:1

FROM python:latest AS build

WORKDIR /app
COPY requirements_ci.txt requirements_ci.txt
RUN pip install -r requirements_ci.txt
COPY . .
RUN python setup.py bdist_wheel

FROM python:latest
COPY --from=build /app/dist/ .
RUN pip install wa_backend-0.0.0.whl
# TODO : To be removed when plugged to external db
COPY scripts/create_db.py .
RUN python create_db.py
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]