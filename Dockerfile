FROM python:3
COPY . /app
WORKDIR /app
RUN apt-get update
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "run_server.py", "127.0.0.1:5000"]

