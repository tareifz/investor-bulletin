""" Alert DAL"""
"""_summary_
this file is to right any ORM logic for the Alert model
"""
from db.models import Alert
from resources.alert.alert_schema import AlertCreate
from sqlalchemy.orm import Session


# Get all, limitless 🫢
def get_all(db: Session):
    return db.query(Alert).all()


# Create alert
def create_alert(alert: AlertCreate, db: Session):
    new_alert = Alert(
        name=alert.name,
        threshold_price=alert.threshold_price,
        symbol=alert.symbol,
        price=alert.price,
    )
    db.add(new_alert)
    db.commit()
    db.refresh(new_alert)
    return new_alert
