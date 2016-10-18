.PHONY: clean lint open run

clean:
	find . -name \*.pyc -delete

lint:
	pylint flaskr settings

open:
	open http://127.0.0.1:5000/

run: clean
	flask run
