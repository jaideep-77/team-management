venv:
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt && cd core && python3 manage.py makemigrations && python3 manage.py migrate

server: venv
	. venv/bin/activate && cd core && python3 manage.py runserver
.PHONY: server

clean:
	-rm -r venv
.PHONY: clean
