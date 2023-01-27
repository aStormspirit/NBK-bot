FROM python:3.10-alpine

WORKDIR /app

RUN cd /app

COPY . .

RUN ls

RUN pip install -r requirements.txt

CMD python3 bot.py
