# Use Python as the base image 
FROM python:3.9
# Define the working directory
WORKDIR /app
# Copy the application code into the container
COPY . /app
# Install dependencies
RUN pip install -r requirements.txt
# Expose the application port
EXPOSE 5000
# Set the startup command
CMD ["opentelemetry-instrument", "flask", "run", "--host", "0.0.0.0"]