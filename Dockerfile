FROM ubuntu:20.04
 
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.1.4 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
	PYSETUP_PATH="/opt/website" \
    VENV_PATH="/opt/website/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"
RUN export PATH=$PATH

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
		  python3.9\
		  python3-pip\
		  curl \
		  python3-venv \
		  && rm -rf /var/lib/apt/lists/*
	
WORKDIR $PYSETUP_PATH

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python3
COPY poetry.lock pyproject.toml ./
RUN poetry install --no-dev
RUN pip install gunicorn

#Fixing: https://bugs.launchpad.net/ubuntu/+source/tzdata/+bug/1899343
RUN echo "Etc/UTC" > /etc/timezone

COPY . .
