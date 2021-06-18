#!/usr/bin/python
import logging
from logging.handlers import SMTPHandler

from app import app

if __name__ == "__main__":
    app.run()
