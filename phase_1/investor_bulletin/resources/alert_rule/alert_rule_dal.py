""" Alert Rule  DAL"""
"""_summary_
this file is to right any ORM logic for the Alert Rule model
"""
from resources.alert_rule.alert_rule_schema import AlertRuleCreate, AlertRulePatch
from db.models import AlertRule
from sqlalchemy.orm import Session


# Get by id
def get_rule_by_id(id, db: Session):
    return db.get(AlertRule, id)


def get_rule_by_symbol_and_price(symbol, price, db):
    return (
        db.query(AlertRule)
        .filter(AlertRule.symbol == symbol)
        .filter(AlertRule.threshold_price == price)
        .first()
    )


# Create rule
def create_alert_rule(rule: AlertRuleCreate, db: Session):
    new_rule = AlertRule(
        name=rule.name, threshold_price=rule.threshold_price, symbol=rule.symbol
    )
    db.add(new_rule)
    db.commit()
    db.refresh(new_rule)
    return new_rule


# Get all, limitless 🫢
def get_all_alert_rules(db: Session):
    return db.query(AlertRule).all()


# Delete rule
def delete_alert_rule(rule: AlertRule, db: Session):
    db.delete(rule)
    db.commit()


# Partilly update rule
def patch_alert_rule(id: int, rule: AlertRulePatch, db: Session):
    obj = rule.model_dump(exclude_unset=True)
    db.query(AlertRule).filter(AlertRule.id == id).update(dict(obj))
    db.commit()
    return get_rule_by_id(id, db)
