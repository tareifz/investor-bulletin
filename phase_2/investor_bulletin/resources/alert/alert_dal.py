""" Alert DAL"""
"""_summary_
this file is to right any ORM logic for the Alert model
"""
from db.models import Alert
from sqlalchemy.orm import Session


# Get all, limitless 🫢
def get_all(db: Session):
    return db.query(Alert).all()
