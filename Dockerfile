FROM python:3

# Set a directory for the app.
WORKDIR /usr/src/app

# Copy all the files to the container.
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Define the posrt number the container should expose.
EXPOSE 8000

# Run the sever.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]