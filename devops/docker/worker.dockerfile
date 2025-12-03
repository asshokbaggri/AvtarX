FROM python:3.10-slim

WORKDIR /worker

COPY ../../backend /worker

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "worker.py"]
