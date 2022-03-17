from models import db
from auth import login_manager


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String())
    lastname = db.Column(db.String())
    email = db.Column(db.String(), unique=True)
    password = db.Column(db.String())
    is_active= db.Column(db.Boolean(), default=True)

    def get_id(self):
        return self.id


@login_manager.user_loader
def user_loader(id):
    user = User.query.get(id)
    return user