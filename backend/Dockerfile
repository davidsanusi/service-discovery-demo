# Use the Python3.7.2 image
FROM docker.io/davidsanusi/nginx-uwsgi-alpine3.9 

RUN apk add gcc musl-dev

# Set the working directory to /app
WORKDIR /app

# Add requirements file before adding the rest of the app folder
# to allow layer caching optimization
ADD requirements.txt /app

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
ADD . /app

# Expose port 80
EXPOSE 80

# run the command to start uWSGI
CMD ["/usr/bin/supervisord"]