all: install test run deploy

install:
	@echo "Installing pipenv and pip dependencies..."
	pip install pipenv
	pipenv --python 3.7
	pipenv install requests
	pipenv install ntplib
	pipenv install pytest
	
test:
	@echo "Testing..."
	# pipenv run pytest tests/tests.py >> results.txt
	
run: 
	@echo "Running app..."
	pipenv run python app.py append >> results.txt
	
deploy:
	@echo "Updating results.txt on git..."
	git add .
	git commit -m "Changed in results.txt"
	git push