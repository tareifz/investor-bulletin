""" Alert Service"""
"""_summary_
this file to write any business logic for the Alerts
"""
from resources.alert.alert_schema import AlertCreate
from resources.alert.alert_dal import get_all


def get_all_alerts(db):
    return get_all(db=db)
