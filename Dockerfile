FROM python:3.14-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 72

ENTRYPOINT ["python3"]
CMD ["src/main.py"]