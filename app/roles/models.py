from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import Schema, fields, validate
from app.users.models import db

class Roles(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True, server_default = 'normal', nullable=False)

    def __init__(self, name):
         self.name=name

    def add(self,role):
        db.session.add(role)
        return session_commit ()

    def update(self):
         return session_commit()

    def delete(self,role):
        db.session.delete(role)
        return session_commit()

class RolesSchema(Schema):

    not_blank = validate.Length(min=1, error='Field cannot be blank')
    name = fields.String(validate=not_blank)


    class Meta:
       fields = ('id', 'name')

def  session_commit ():
      try:
        db.session.commit()
      except SQLAlchemyError as e:
         db.session.rollback()
         reason=str(e)
         return reason
