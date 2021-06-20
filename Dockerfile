FROM debian:sid-slim

# Install Python
USER root
RUN apt-get update && apt-get install python3-distutils wget -y
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py
RUN python3 -m pip install selenium


# Install Firefox and Geckodriver
RUN apt-get update                             \
 && apt-get install -y --no-install-recommends \
    ca-certificates curl firefox               \
 && rm -fr /var/lib/apt/lists/*                \
 && curl -L https://github.com/mozilla/geckodriver/releases/download/v0.28.0/geckodriver-v0.28.0-linux64.tar.gz | tar xz -C /usr/local/bin \
 && apt-get purge -y ca-certificates curl

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN pip install -r requirements.txt

# Run the web service on container startup.
CMD exec gunicorn --bind :3000 --workers 1 --threads 8 wsgi:app
