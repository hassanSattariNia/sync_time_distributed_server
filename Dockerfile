FROM python:3.12-slim

COPY . .

CMD ["python","./run.py"]