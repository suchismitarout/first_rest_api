FROM python:3
ADD first_restapi /app
WORKDIR /app
RUN apt-get update
RUN pip install -r requirements.txt
EXPOSE 5000/tcp
EXPOSE 5000/udp
CMD python run_server.py

