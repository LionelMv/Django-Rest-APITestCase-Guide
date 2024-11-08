# Makefile contains commands to run various tests

.PHONY: test_jwt_views
test_jwt_views:
	@echo "Running test_jwt_views..."
	coverage run manage.py test kitabu.tests.test_jwt_views

.PHONY: test_models
test_models:
	@echo "Running test_models..."
	coverage run manage.py test kitabu.tests.test_models

.PHONY: test_views
test_views:
	@echo "Running test_views..."
	coverage run manage.py test kitabu.tests.test_views
