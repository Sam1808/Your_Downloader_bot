FROM python:3.10

WORKDIR /app
COPY . .

RUN apt-get update \
    && apt-get install -y build-essential \
    && apt-get install -y clang \
    && apt-get install -y python3-dev \
    && pip install -r requirements.txt --no-cache-dir --upgrade

CMD python yd_bot.py