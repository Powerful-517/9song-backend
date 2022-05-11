FROM python:3.9-alpine as build
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories \
    && apk update \
    && apk add git gcc g++ musl-dev libffi-dev libressl-dev make
WORKDIR /install
COPY requirements.txt /install/requirements.txt
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r /install/requirements.txt \
    && mkdir -p /install/lib/python3.9/site-packages \
    && cp -rp /usr/local/lib/python3.9/site-packages /install/lib/python3.9 \
    && cp -p /usr/local/bin/uvicorn /install/uvicorn


FROM python:3.9-alpine

# This hack is widely applied to avoid python printing issues in docker containers.
# See: https://github.com/Docker-Hub-frolvlad/docker-alpine-python3/pull/13
ENV PYTHONUNBUFFERED=1

COPY --from=build /install/lib /usr/local/lib
COPY --from=build /install/uvicorn /usr/local/bin/uvicorn

WORKDIR /code
