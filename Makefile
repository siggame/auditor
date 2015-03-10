BOOTSTRAP_URL=http://downloads.buildout.org/2/bootstrap.py

.PHONY: default clean very-clean

# Runs buildout
default: bin/buildout
	python bin/buildout

# Runs bootstrap
bin/buildout: bootstrap.py
	mkdir -p var/
	python bootstrap.py

# Gets bootstrap
bootstrap.py:
	wget $(BOOTSTRAP_URL)

# Destroys existing test database and creates a new one
db:
	rm -f var/db/*.sqlite3
	python bin/django migrate

test: bin/buildout
	python bin/buildout install simple-django
	python bin/nosey

clean:
	find ./ -name *.pyc -delete
	find ./ -name *.~ -delete
