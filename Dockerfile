FROM tiangolo/uvicorn-gunicorn:python3.10-slim

USER root

COPY requirements.txt .
RUN python3 -m pip install --no-cache-dir -r requirements.txt

WORKDIR /ms
COPY app /ms/app
COPY main.py /ms/

EXPOSE 8108

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8108"]