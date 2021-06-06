# syntax=docker/dockerfile:1

FROM python:latest

RUN apt-get install -y git

# WORKDIR /app

RUN git clone git://github.com/lizzieb1416/wa_backend.git


WORKDIR ./wa_backend

RUN pip install . --use-feature=in-tree-build
# TODO : To be removed when plugged to external db
RUN python scripts/create_db.py

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]