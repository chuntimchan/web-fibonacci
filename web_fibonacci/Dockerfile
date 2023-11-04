FROM python:3.9-slim

WORKDIR /app

COPY fibonacci.py .
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install argparse

ENTRYPOINT ["python", "fibonacci.py"]

