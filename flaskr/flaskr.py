import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
SETTINGS_DIR = os.path.join(BASE_DIR, 'settings')
app.config.from_pyfile(os.path.join(SETTINGS_DIR, 'default.py'))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv
