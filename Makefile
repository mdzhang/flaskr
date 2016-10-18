.PHONY: clean lint open run setup_db

clean:
	find . -name \*.pyc -delete

lint:
	pylint flaskr settings

open:
	open http://127.0.0.1:5000/

run: clean
	flask run

setup_db:
	sqlite3 /tmp/flaskr.db < flaskr/schema.sql
	flask initdb
