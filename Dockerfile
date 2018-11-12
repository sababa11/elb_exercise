# Use an official Python runtime as a parent image
FROM tiangolo/uwsgi-nginx-flask:python2.7

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD app /app

# copy over our requirements.txt file
COPY requirements.txt /tmp/

# Install any needed packages specified in requirements.txt
RUN pip install -U pip
RUN pip install --trusted-host pypi.python.org -r /tmp/requirements.txt
# RUN apt-get update && apt-get install -y curl
# RUN apt update && apt install -y net-tools

# Make port 8090 available to the world outside this container
EXPOSE 8090

# Define environment variable
# ENV FLASK_ENV development
# ENV FLASK_DEBUG 1

# Run app.py when the container launches
CMD ["python", "/app/demo_app.py"]
