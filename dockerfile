# syntax=docker/dockerfile:1

FROM python:latest

COPY ./dist/wa_backend-0.1-py2.py3-none-any.whl .
RUN pip install wa_backend-0.1-py2.py3-none-any.whl

# TODO : To be removed when plugged to external db
COPY scripts/create_db.py .
RUN python create_db.py

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]