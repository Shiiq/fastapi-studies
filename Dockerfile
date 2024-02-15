FROM python:3.12.1-alpine3.19 as base

# python:
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# pip:
ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

# poetry:
ENV POETRY_VERSION=1.6.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1

# paths:
ENV PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"


FROM base as builder

RUN apk update && apk add --no-cache gcc musl-dev libffi-dev

WORKDIR $PYSETUP_PATH

COPY pyproject.toml ./

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir setuptools wheel \
    && pip install --no-cache-dir "poetry==$POETRY_VERSION"

RUN poetry install --no-interaction --no-ansi --no-root


FROM base as deployment

COPY --from=builder $PYSETUP_PATH $PYSETUP_PATH

WORKDIR FastAPI-Studies

ENV PYTHONPATH="$PYTHONPATH/FastAPI-Studies/src"

COPY ./ ./

#RUN pip install -e .

ENTRYPOINT ["./start.sh"]
