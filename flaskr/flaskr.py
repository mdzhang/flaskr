import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, jsonify

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


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print 'Initialized the database.'


@app.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('select title, text from entries order by id desc')
    entries = cur.fetchall()
    return jsonify(map(lambda entry: {'title': entry['title'], 'text': entry['text']}, entries))


@app.route('/add', methods=['POST'])
def add_entry():
    json = request.get_json()
    db = get_db()
    db.execute('insert into entries (title, text) values (?, ?)',
               [json['title'], json['text']])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))
