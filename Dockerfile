FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

# Install node prereqs, nodejs and yarn
# Ref: https://deb.nodesource.com/setup_12.x
# Ref: https://yarnpkg.com/en/docs/install
#RUN \
#  apt-get update && \
#  apt-get install -yqq nodejs yarn libmemcached-dev && \
#  pip install -U pip

# Install Chrome for Selenium
RUN curl https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o /chrome.deb
RUN dpkg -i /chrome.deb || apt-get install -yf
RUN rm /chrome.deb

# Install chromedriver for Selenium
RUN curl https://chromedriver.storage.googleapis.com/2.31/chromedriver_linux64.zip -o /usr/local/bin/chromedriver
RUN chmod +x /usr/local/bin/chromedriver

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN pip install -r requirements.txt

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 wsgi:app