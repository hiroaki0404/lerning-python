FROM python:3.10-slim

COPY templates/ /app/templates/
COPY main.py requirements.txt /app/
RUN pip install -r /app/requirements.txt

EXPOSE 5000
CMD ["python3", "/app/main.py"]
