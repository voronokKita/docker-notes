FROM python:3.11-slim-buster

RUN apt update && apt -y install gcc libpq-dev curl
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /notes
COPY requirements.txt .
RUN pip3 install -r requirements.txt

WORKDIR /notes/app
COPY ./app .
CMD ["python3", "-O", "__init__.py"]
