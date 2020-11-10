#to install packages, type: make packages
packages: requirements.txt
	pip install -r requirements.txt
#to run the app, type: make app
app : insurance.csv
	python app.py
#if you want to clean the packages and app files, type: make clean
.PHONY: clean
clean:
	rm app 
