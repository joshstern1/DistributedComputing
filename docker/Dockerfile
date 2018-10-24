FROM alpine:3.5

RUN apk update
RUN apk add --no-cache python3 python3-dev build-base openssl
RUN pip3 install --upgrade pip
RUN rm -r /root/.cache && mkdir -p /app

COPY server.py flaskapp.py flaskapp2.py requirements.txt /app/
WORKDIR /app
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["worker.py"]
