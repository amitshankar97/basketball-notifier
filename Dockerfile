FROM python:3

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY ./close_game.py /app/close_game.py

ENV DB_CONN_STRING ''
ENV MAKER_URL ''

CMD python close_game.py

# docker build -t basketball-notifier ./ && docker run -it --rm basketball-notifier