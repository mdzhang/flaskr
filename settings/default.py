"""Default project settings"""

import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
DATABASE = os.path.join(BASE_DIR, *['flaskr', 'flaskr.db'])
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
