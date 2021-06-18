FROM python:buster
MAINTAINER Nikolai R Kristiansen <nikolaik@gmail.com>

# Install node prereqs, nodejs and yarn
# Ref: https://deb.nodesource.com/setup_12.x
# Ref: https://yarnpkg.com/en/docs/install
#RUN \
#  apt-get update && \
#  apt-get install -yqq nodejs yarn libmemcached-dev && \
#  pip install -U pip

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install yarn
# RUN yarn install

# Install production dependencies.
RUN pip install -r requirements.txt

# Build assets
# RUN flask assets build

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 wsgi:app