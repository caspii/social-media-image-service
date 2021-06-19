# -*- coding: UTF-8 -*-
from flask import Flask, request, send_file

app = Flask(__name__)


@app.route('/')
def view_landing():
    return "Welcome to screenshot service"

@app.route('/preview_image/<token>.png')
def preview_image(token):
    """
    Returns an image (PNG) of the given scoreboard, so that it can be shown on social media as a preview
    """

    from splinter import Browser
    from selenium.webdriver.chrome.options import Options
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--hide-scrollbars')
    if app.config["ENV"] == "production":
        executable_path = {'executable_path': '/usr/bin/chromedriver'}
    else:
        executable_path = {'executable_path': '/opt/homebrew/bin/chromedriver'}
    browser = Browser('chrome', headless=True, options=chrome_options, **executable_path)
    browser.driver.set_window_size(1200, 630)
    url = f'https://keepthescore.co/board/{token}/'
    browser.visit(url)
 #   logging.debug(f'Opengraph preview image: visiting {url}')
    temp_dir = '/tmp/'
    path = f'{temp_dir}{token}'
    screenshot_path = browser.screenshot(path)
  #  logging.info(f'Generated social media preview image {token}')
    return send_file(screenshot_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(port=5001, debug=True)