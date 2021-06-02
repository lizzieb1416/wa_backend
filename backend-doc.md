

## Virtual envirorment and dependencies
In the terminal of the folder project (wa_backend)

- python -m venv .venv
- .venv\Scripts\activate

- pip install flask flask-sqlalchemy
- pip install 
- pip install -U flask-cors
- pip freeze > requirements.txt

## Creating the app
touch api.py

## Run server
Python api.py --> Runs in port 5000

## DB config
python 
from api import db
db.create_all()

## STEPS AFTER CLONING REPOSITORY FROM GITHUB 

1. Create and activate envirornement 
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt 
2. Set up DB 
python 
from api import db
db.create_all()
exit()
3. run the api
python api.py
4. See the frontend documentation to set up after cloning 

## POSTGRESQL 
https://www.youtube.com/watch?v=XZ_gAWdGzZk

https://www.youtube.com/watch?v=w25ea_I89iM

https://www.youtube.com/watch?v=3HPq12w-dww&list=PLIWLW8_gNNc1dLUGuSAzpsf3zRDrR-yKy&index=65

## ENV VARIABLES
https://itnext.io/start-using-env-for-your-flask-project-and-stop-using-environment-variables-for-development-247dc12468be

https://hackingandslacking.com/configuring-your-flask-application-4e5341d7affb



