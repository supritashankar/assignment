assignment
==========
[![Build Status](https://travis-ci.org/supritashankar/assignment.png?branch=master)](https://travis-ci.org/supritashankar/assignment)

## Setup ENV

            mkvirtualenv assignment 
            pip install -r requirements/base.txt

## Setup DB

* Create DB
  
  	``` python manage.py syncdb ```

* Create dummy data

  	``` http://127.0.0.1:8000/admin/portfolio/ ```

## View Results

* Update and view previous data

  	``` http://127.0.0.1:8000/clientui/results/ ```

* More user friendly

  	``` http://127.0.0.1:8000/clientui/colors/ ```

## Tests

* Some initial tests

	``` python manage.py test ```

## License

* MIT licensed
