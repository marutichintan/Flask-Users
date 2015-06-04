from werkzeug.security import generate_password_hash
from sqlalchemy.exc import SQLAlchemyError

from app import create_app
from app.users.models import Users, Roles, db

app = create_app('config')

name='Leo'
email='youremail@leog.in'
password=generate_password_hash('password')
is_enabled=True
role="admin"
user=Users(email, name,password, is_enabled)

def db_commit():
    try:
          db.session.commit()
          print("{} was added successfully".format(email))
          return True
    except SQLAlchemyError as e:
          reason=str(e)
          print (reason)
          return False

with app.app_context():
    new_role = Roles(role)
    db.session.add(new_role)
    if db_commit():
        user_role = Roles.query.filter_by(name=role).first()
        user.roles.append(user_role)
        db.session.add(user)
        db_commit()
