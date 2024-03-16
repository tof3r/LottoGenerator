FROM tiangolo/uwsgi-nginx-flask:python3.11
WORKDIR /lotto
ENV STATIC_URL /app/static
ENV STATIC_PATH ./app/static
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt