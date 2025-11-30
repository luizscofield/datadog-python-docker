FROM python:3.11-slim

WORKDIR /app

COPY app.py requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV DD_SERVICE="python-app-c" \
    DD_ENV="dev" \
    DD_LOGS_INJECTION=true

CMD ["ddtrace-run", "python", "app.py"]
