# -*- coding: UTF-8 -*-
from flask import Flask, request, send_file
from splinter import Browser

app = Flask(__name__)


@app.route('/')
def view_landing():
    return "Welcome to the screenshot service!"
    logging.info(f'Root url called')

@app.route('/render.png')
def preview_image(token=34):
    """
    Returns an image (PNG) of the given scoreboard, so that it can be shown on social media as a preview
    """
    url = request.args.get('url', default='https://casparwre.de', type=str)
    browser = Browser('firefox', headless=True)
    #browser.driver.set_window_size(1200, 630)
    #url = f'https://keepthescore.co/board/{token}/'
    # url = 'https://keepthescore.co'
    browser.visit(url)
 #   logging.debug(f'Opengraph preview image: visiting {url}')
    temp_dir = '/tmp/'
    path = f'{temp_dir}{token}'
    screenshot_path = browser.screenshot(path)
  #  logging.info(f'Generated social media preview image {token}')
    return send_file(screenshot_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(port=5001, debug=True)