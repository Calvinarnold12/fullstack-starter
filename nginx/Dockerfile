FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY django-helloworld/requirements.txt /code/
RUN pip install -r requirements.txt

# Copy project
COPY django-helloworld /code/

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
