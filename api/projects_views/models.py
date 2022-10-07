import uuid

from common.models import BaseModel
from registrations.build_app import db


def generate_uuid():
    return str(uuid.uuid4())

#database model for weekly_reports


class Project(BaseModel):

    __tablename__ = 'Project'
    project_id = db.Column(db.Integer, unique = True)
    name = db.Column(db.String)
    t_m_and_fixed_cost = db.Column(db.Float)
    duration = db.Column(db.Integer)
    weekly_completion = db.Column(db.Float)
    start_date = db.Column(db.DateTime)
    no_of_resources = db.Column(db.Integer)
    overall_complition = db.Column(db.Float)

class Weekly_reports(BaseModel):
    __table_name__ = "weekly_reports"
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    no_stories = db.Column(db.Integer)
    features_completed = db.Column(db.Float)
    no_bugs = db.Column(db.Float)
    bugs_complete = db.Column(db.Integer)
    is_code_review = db.Column(db.Boolean)
    is_unit_testing = db.Column(db.Boolean)
    weekly_communication = db.Column(db.Boolean)
    migration = db.Column(db.VARCHAR)
    risk = db.Column(db.VARCHAR)
    risk_migration = db.Column(db.VARCHAR)
    support_required = db.Column(db.Boolean)
    project_id = db.Column(db.Integer, db.ForeignKey('Project._id'))

