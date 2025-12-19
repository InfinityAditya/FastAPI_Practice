# base image
FROM python:3.11-slim

# workdir
WORKDIR /app

# copy
COPY requirements.txt .
RUN pip install --no-cache-dir -r  requirements.txt

# copy
COPY . .


# port
EXPOSE 8000

# command to start FastSPI application
CMD ["uvicorn","app:app", "--host","0.0.0.0", "--port", "8000"]