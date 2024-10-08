FROM python:3.11-slim

WORKDIR /todo_backend

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /todo_backend

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]      
 