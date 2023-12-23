from typing import Annotated
from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from db.models import get_db
from resources.alert_rule.alert_rule_service import (
    delete_rule,
    get_all_rules,
    create_new_rule,
    patch_rule,
)
from resources.alert_rule.alert_rule_schema import (
    AlertRule,
    AlertRuleCreate,
    AlertRulePatch,
)


router = APIRouter()


# Get all
@router.get("/", response_model=list[AlertRule])
def get_all_rules_route(db: Session = Depends(get_db)):
    return get_all_rules(db)


# Create
@router.post("/", response_model=AlertRule)
def post_rules_route(rule: AlertRuleCreate, db: Session = Depends(get_db)):
    return create_new_rule(rule, db)


# Partial update
@router.patch("/{id}")
def patch_rules_route(
    id: Annotated[int, Path(title="The ID of the alert rule to update")],
    rule: AlertRulePatch,
    db: Session = Depends(get_db),
):
    return patch_rule(id, rule, db)


# Delete
@router.delete("/{id}")
def delete_rules_route(
    id: Annotated[int, Path(title="The ID of the alert rule to delete")],
    db: Session = Depends(get_db),
):
    return delete_rule(id, db)
