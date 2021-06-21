# -*- coding: UTF-8 -*-
from flask import Flask, send_file
from splinter import Browser

app = Flask(__name__)


@app.route('/')
def view_landing():
    return "Welcome to the screenshot service!"
    app.logger.info(f'Root url called')

@app.route('/<token>.png')
def preview_image(token):
    """
    Returns an image (PNG) of the given scoreboard, so that it can be shown on social media as a preview
    """
    #url = request.args.get('url', default='https://casparwre.de', type=str)
    browser = Browser('firefox', headless=True)
    browser.driver.set_window_size(1200, 630)
    url = f'https://keepthescore.co/board/{token}/'
    browser.visit(url)
    app.logger.info(f'Opengraph preview image: visiting {url}')
    temp_dir = '/tmp/'
    path = f'{temp_dir}{token}'
    screenshot_path = browser.screenshot(path)
    app.logger.info(f'Generated social media preview image {token}')
    return send_file(screenshot_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(port=5001, debug=True)