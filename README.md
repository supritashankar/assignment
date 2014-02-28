assignment
==========

To update data:
curl --dump-header - -H "Content-Type: application/json" -X PUT --data '{"color": "R"}' http://127.0.0.1:8000/api/color/2/\?format\=json
