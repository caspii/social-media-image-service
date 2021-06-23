# -*- coding: UTF-8 -*-
import os
import urllib.parse
from flask import Flask, send_file, abort
from splinter import Browser

app = Flask(__name__)
browser = Browser('firefox', headless=True)


@app.route('/')
def view_landing():
    return "Welcome to the screenshot service!"


@app.route('/image/<path:encoded_url>.png')
def generate_image(encoded_url):
    """
    Returns an image (PNG) of a URL. The URL is encoded in the path of the image being requested.
    """
    url_to_fetch = urllib.parse.unquote_plus(encoded_url)
    domain = os.environ.get('DOMAIN', 'https://casparwre.de')
    if not url_to_fetch.startswith(domain):
        app.logger.info(f'Not allowed to generate preview for this domain: {url_to_fetch}')
        abort(405)
    app.logger.debug(f'Generating preview for {url_to_fetch}')
    browser.driver.set_window_size(1200, 630)
    browser.visit(url_to_fetch)
    screenshot_path = '/tmp/'
    screenshot = browser.screenshot(screenshot_path)
    return send_file(screenshot, mimetype='image/png')


@app.route('/<token>.png')
def generate_keepthescore_image(token):
    """
    Legacy route for keepthescore.
    """
    url = f'https://keepthescore.co/board/{token}/'
    browser.driver.set_window_size(1200, 630)
    browser.visit(url)
    app.logger.info(f'Preview image: visiting {url}')
    temp_dir = '/tmp/'
    path = f'{temp_dir}{token}'
    screenshot_path = browser.screenshot(path)
    return send_file(screenshot_path, mimetype='image/png')


if __name__ == '__main__':
    app.run(port=5001, debug=True)