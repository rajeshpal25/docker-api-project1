FROM python:3.10-slim
WORKDIR /app_v1
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app_v1.py .
CMD ["python", "app_v1.py"]
