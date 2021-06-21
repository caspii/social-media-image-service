# -*- coding: UTF-8 -*-
import time

from flask import Flask, send_file
from splinter import Browser

app = Flask(__name__)
browser = Browser('firefox', headless=True)


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
    tic = time.perf_counter()
    url = f'https://keepthescore.co/board/{token}/'
    #browser = Browser('chrome', headless=False, incognito=True)
    browser.driver.set_window_size(1200, 630)
    browser.visit(url)
    app.logger.info(f'Opengraph preview image: visiting {url}')
    temp_dir = '/tmp/'
    path = f'{temp_dir}{token}'
    screenshot_path = browser.screenshot(path)
    #browser.quit()
    toc = time.perf_counter()
    app.logger.info(f'Generated image for {token}. Time={toc-tic:0.4f} secs')
    return send_file(screenshot_path, mimetype='image/png')


if __name__ == '__main__':
    app.run(port=5001, debug=True)