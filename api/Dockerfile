FROM python:3.12 as base

ENV VIRTUAL_ENV=/opt/venv

RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt schema.graphql .

RUN pip install -r requirements.txt

ENTRYPOINT ["flask", "--app", "api:app", "run", "--host", "0.0.0.0", "--port", "8000"]