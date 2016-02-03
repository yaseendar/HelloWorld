Installation
------------

    git clone https://github.com/yaseendar/HelloWorld.git

    cd HelloWorld

    pip install -r requirements.txt #assume you are in a virtual environment

    python manage.py migrate


Api calls
------------

1. Generate dummy token

curl -X GET http://127.0.0.1:8000/api/dummytoken/



2. Get all names present in database

curl -X GET http://127.0.0.1:8000/api/display/allnames/ -H 'Authorization: Token  YOUR DUMMY TOKEN'

