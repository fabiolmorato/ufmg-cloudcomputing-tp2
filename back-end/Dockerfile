FROM python:3.10

WORKDIR /app
COPY . .
RUN chmod +x run.sh

RUN ./run.sh install

CMD ["./run.sh", "run", "download", "start"]
