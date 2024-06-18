FROM registry.fedoraproject.org/fedora-minimal:39 AS base


RUN microdnf -y upgrade &&  microdnf -y install python pip shadow-utils supervisord

RUN useradd -m -d /app appuser


FROM base AS Django

WORKDIR /app/

COPY pyproject.toml poetry.lock /app/
COPY backend/ /app/

RUN pip install --upgrade pip poetry setuptools
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi
# RUN pipenv run /app/django/manage.py migrate
# USER appuser

CMD ["/usr/bin/supervisord"]
