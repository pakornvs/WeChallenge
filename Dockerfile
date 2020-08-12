FROM node:12

WORKDIR /nodebuild
copy frontend /nodebuild
RUN npm install && npm run build

FROM python:3.7

ARG USERNAME=app
ARG APPDIR=/app

WORKDIR $APPDIR
COPY --from=0 /nodebuild/build $APPDIR/build
COPY backend $APPDIR

RUN pip --disable-pip-version-check --no-cache-dir install -r requirements.txt

RUN useradd $USERNAME && chown -R $USERNAME $APPDIR

USER $USERNAME

RUN python manage.py collectstatic --noinput
