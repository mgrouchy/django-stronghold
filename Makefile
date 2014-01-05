test:
	python test_project/manage.py test --settings=test_project.settings stronghold.tests
update-pypi:
	python setup.py sdist upload
	python setup.py bdist_wheel upload
