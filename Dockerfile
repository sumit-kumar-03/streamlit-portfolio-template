##********************** MAIN BUILD **********************##
FROM python:3.12-slim


# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1


# Set the working directory
WORKDIR /usr/src/app


# Copy requirements
COPY ./requirements.txt ./requirements.txt


# Install dependencies and bash/inotify-tools
RUN apt-get update && \
    apt-get install -y inotify-tools && \
    pip install -r requirements.txt 



# Default entrypoint
ENTRYPOINT ["tail", "-f", "/dev/null"]
