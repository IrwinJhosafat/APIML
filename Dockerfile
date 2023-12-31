FROM python:3.9

WORKDIR /app
COPY requirements.txt .

COPY *.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]