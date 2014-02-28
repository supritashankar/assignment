assignment
==========

Setup ENV
--------
Step 1: mkvirtualenv assginment
Step 2: pip install -r requirements/base.txt
=======
Step 1: mkvirtualenv assginment <br/>
Step 2: pip install requirements/base.txt
>>>>>>> d3b16f6981f596ee5c797232e1f133e028a4171f

Setup DB
--------
Step 3: python manage.py syncdb <br/>
Step 4: http://127.0.0.1:8000/admin/portfolio/ -> create dummy data

View Results
------------
Step 5: http://127.0.0.1:8000/clientui/results/ -> to view colors <br/>
Step 6: To update data: <br/>
curl --dump-header - -H "Content-Type: application/json" -X PUT --data '{"color": "R"}' http://127.0.0.1:8000/api/color/2/\?format\=json
