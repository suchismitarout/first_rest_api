FROM python:3
COPY . /app
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN apt-get update
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "run_server.py", "127.0.0.1:5000"]

