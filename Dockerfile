FROM python:latest
WORKDIR /app
COPY shreyas.py /app/
CMD ["python", "shreyas.py"]