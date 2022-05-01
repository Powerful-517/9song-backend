FROM python:3.9-alpine
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories \
    && apk update \
    && apk add git gcc g++ musl-dev libffi-dev libressl-dev make
WORKDIR /install
COPY requirements.txt /requirements.txt
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r /requirements.txt \
    && mkdir -p /install/lib/python3.9/site-packages \
    && cp -rp /usr/local/lib/python3.9/site-packages /install/lib/python3.9



FROM python:3.9-alpine

# This hack is widely applied to avoid python printing issues in docker containers.
# See: https://github.com/Docker-Hub-frolvlad/docker-alpine-python3/pull/13
ENV PYTHONUNBUFFERED=1

COPY --from=0 /install/lib /usr/local/lib
#COPY --from=0 /install/src /usr/local/src
WORKDIR /app

#CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]

