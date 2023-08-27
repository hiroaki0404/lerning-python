FROM python:3.10-slim

COPY templates/ /app/templates/
COPY main.py requirements.txt /app/
RUN pip install -r /app/requirements.txt && \
    opentelemetry-bootstrap -a install

EXPOSE 5000
ENV FLASK_APP app.main.py
CMD opentelemetry-instrument --traces_exporter otlp --metrics_exporter console \
    --service_name hit-and-blow --exporter_otlp_protocol grpc flask run --host=0.0.0.0
