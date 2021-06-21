# Script to run flask app without docker

source venv/bin/activate  # Activate virtual env
export FLASK_APP=app.py
export WERKZEUG_DEBUG_PIN=off
export FLASK_ENV='development'
flask run --host=0.0.0.0 --port=5001