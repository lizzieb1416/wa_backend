from wa_backend import create_app
from wa_backend.apis.tasks import db

app = create_app()

with app.app_context():
    
    db.create_all()
