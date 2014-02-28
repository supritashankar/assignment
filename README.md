assignment
==========

Setup ENV
--------
Step 1: mkvirtualenv assginment
Step 2: pip install requirements/base.txt

Setup DB
--------
Step 3: python manage.py syncdb
Step 4: http://127.0.0.1:8000/admin/portfolio/ -> create dummy data

View Results
------------
Step 5: http://127.0.0.1:8000/clientui/results/ -> to view colors
Step 6: To update data:
curl --dump-header - -H "Content-Type: application/json" -X PUT --data '{"color": "R"}' http://127.0.0.1:8000/api/color/2/\?format\=json
