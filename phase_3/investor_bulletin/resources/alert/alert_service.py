""" Alert Service"""
"""_summary_
this file to write any business logic for the Alerts
"""
from resources.alert.alert_schema import AlertCreate
import resources.alert.alert_dal as data


def get_all_alerts(db):
    return data.get_all(db=db)


# Create alert
def create_alert(alert: AlertCreate, db):
    return data.create_alert(alert, db)
