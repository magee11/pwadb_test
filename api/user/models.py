from common.models import BaseModel
from registrations.build_app import db

class User(BaseModel):
    
    __tablename__ = "user_table"
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    is_super_admin = db.Column(db.Boolean, nullable=False)
    delete_permission = db.Column(db.Boolean, nullable=False)
    edit_permission = db.Column(db.Boolean, nullable=False)
    password_hash = db.Column(db.String(255))

