FROM python:3.7

ARG USERNAME=app
ARG APPDIR=/app

COPY requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
   && rm -rf /tmp/pip-tmp

WORKDIR $APPDIR
COPY . $APPDIR

RUN useradd $USERNAME && chown -R $USERNAME $APPDIR

USER $USERNAME

RUN python manage.py collectstatic --noinput
