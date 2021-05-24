

<< Virtual envirorment and dependencies >>
In the terminal of the folder project (wa_backend)

- python -m venv .venv
- .venv\Scripts\activate

- pip install flask flask-sqlalchemy
- pip install 
- pip install -U flask-cors
- pip freeze > requirements.txt

<< Creating the app >>
touch api.py

<< Run server >>
Python api.py --> Runs in port 5000

<< DB config >>
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
3. See the frontend documentation to set up after cloning 


