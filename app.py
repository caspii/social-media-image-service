# -*- coding: UTF-8 -*-
from flask import Flask, request, send_file

app = Flask(__name__)


@app.route('/')
def view_landing():
    return "Welcome to screenshot service"
    logging.info(f'Root url called')

@app.route('/preview_image/<token>.png')
def preview_image(token):
    """
    Returns an image (PNG) of the given scoreboard, so that it can be shown on social media as a preview
    """

    from splinter import Browser
    browser = Browser('firefox', headless=True)
    #browser.driver.set_window_size(1200, 630)
    #url = f'https://keepthescore.co/board/{token}/'
    url = 'https://cnn.com'
    browser.visit(url)
 #   logging.debug(f'Opengraph preview image: visiting {url}')
    temp_dir = '/tmp/'
    path = f'{temp_dir}{token}'
    screenshot_path = browser.screenshot(path)
  #  logging.info(f'Generated social media preview image {token}')
    return send_file(screenshot_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(port=5001, debug=True)