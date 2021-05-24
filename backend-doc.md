

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
