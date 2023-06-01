FROM python:3.8-slim
WORKDIR /app

ARG DBNAME
ARG DBUSER
ARG DBPASSWORD
ARG DBHOST
ARG APIKEY


RUN apt-get update && \
    apt-get -y install \
    libpq-dev \
    python-dev \
    gcc

RUN pip install --upgrade pip

COPY ./../. /app
RUN sed -i 's#{{USER}}#'$DBUSER'#g' helper.py
RUN sed -i 's#{{PASSWORD}}#'$DBPASSWORD'#g' helper.py
RUN sed -i 's#{{HOST}}#'$DBHOST'#g' helper.py
RUN sed -i 's#{{DB}}#'$DBNAME'#g' helper.py
RUN sed -i 's#{{API_KEY}}#'$APIKEY'#g' helper.py

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]