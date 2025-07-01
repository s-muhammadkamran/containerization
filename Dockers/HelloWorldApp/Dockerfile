# Use this Base image
FROM python:slim-bullseye

# Change my working DIR to /app in container
WORKDIR /HelloWorldApp

# Copy the files from my local to Container
COPY . /HelloWorldApp

# Install the dependencies from requirements.txt
# Use --trusted-host option to avoid SSL issues
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt

# Expose the port
EXPOSE 5000

# Start the application
CMD ["python", "hello-app.py"]

# build the docker image using the below command
## docker build -t UserName/hello-world-web:latest .
## for example 
##   docker build -t msyed/hello-world-web:latest .
## -t = TAG in the docker format 
## dockerhubusername/containername:version
## default version is latest if ommitted

# Run the Docker Container
## docker run -d -p 5000:5000 msyed/hello-world-web