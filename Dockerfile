FROM ubuntu
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev
COPY app/requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt
copy . /app
ENTRYPOINT ["python3", "app.py"]
