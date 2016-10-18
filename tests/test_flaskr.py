"""
    Flaskr Tests
    ~~~~~~~~~~~~
    Tests the Flaskr application.
    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""

import os
import json
import tempfile
import pytest
from flaskr import flaskr

@pytest.fixture
def client(request):
    db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
    flaskr.app.config['TESTING'] = True
    client = flaskr.app.test_client()
    with flaskr.app.app_context():
        flaskr.init_db()

    def teardown():
        os.close(db_fd)
        os.unlink(flaskr.app.config['DATABASE'])
    request.addfinalizer(teardown)

    return client


def test_empty_db(client):
    """Start with a blank database."""
    rv = client.get('/')
    assert json.loads(rv.data) == []
