clean:
	rm -rf build dist *.egg-info

build: clean
	python -m build

install: build
	pip install --force-reinstall dist/*.whl
