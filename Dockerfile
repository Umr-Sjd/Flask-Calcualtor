FROM python:3.11-slim
WORKDIR /calc
COPY . .
RUN pip install flask --no-cache-dir
CMD ["python", "calc.py"]
