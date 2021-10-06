PKG=cluedo
PYTHON=python3
PIP=pip3

default: 
	make python

clean:
	-rm -f *.o
	make pyclean

clean_all:
	make clean
	make pyclean

pyclean:
	-rm -f *.so
	-rm -rf *.egg-info*
	-rm -rf ./tmp/
	-rm -rf ./build/

python:
	${PIP} install -e .

checkdocs:
	${PYTHON} setup.py checkdocs

pypi:
	mkdir -p dist
	touch dist/foobar
	rm dist/*
	${PYTHON} setup.py sdist
	twine check dist/*

upload:
	twine upload dist/*

readme:
	pandoc --from markdown_github --to rst README.md > _README.rst
	sed -e "s/^\:\:/\.\. code\:\: bash/g" _README.rst > README.rst
	rm _README.rst
	rstcheck README.rst

test:
	pytest --cov=${PKG} ${PKG}/tests/
