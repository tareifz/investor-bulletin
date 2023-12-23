""" Alert Rule Service"""
"""_summary_
this file to write any business logic for the Alert Rules
"""
from fastapi import HTTPException
from resources.alert_rule.alert_rule_schema import AlertRuleCreate, AlertRulePatch
from resources.alert_rule.alert_rule_dal import (
    create_alert_rule,
    delete_alert_rule,
    get_all_alert_rules,
    get_rule_by_id,
    get_rule_by_symbol_and_price,
    patch_alert_rule,
)
from resources.market.market_service import get_all_tickers


# This will be used in create and update, the supplied symbol should
# be supported.
def check_valid_ticker(symbol):
    try:
        get_all_tickers().index(symbol)
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="This ticker symbol is not supported.",
        )


# Get rule otherwise return an error as the id must be invalid.
def get_rule(id, db):
    rule = get_rule_by_id(id, db)
    if not rule:
        raise HTTPException(status_code=400, detail="No alert rule with the given ID.")

    return rule


# Create rule
def create_new_rule(rule: AlertRuleCreate, db):
    check_valid_ticker(rule.symbol)

    # No need to create a rule with the same symbol and price unless
    # we support rules per user we will limit to the user.
    alert_rule = get_rule_by_symbol_and_price(
        symbol=rule.symbol, price=rule.threshold_price, db=db
    )
    if alert_rule:
        raise HTTPException(
            status_code=400,
            detail="Alert rule already created for the same symbol and price.",
        )
    return create_alert_rule(rule=rule, db=db)


# Get all
def get_all_rules(db):
    return get_all_alert_rules(db)


# Delete rule
def delete_rule(id, db):
    rule = get_rule(id, db)  # we check if the id is valid.

    delete_alert_rule(rule, db)
    return rule


# Partial update
def patch_rule(id, rule_data: AlertRulePatch, db):
    if rule_data.symbol:  # if we update the symbol check if it is a valid one.
        check_valid_ticker(rule_data.symbol)

    get_rule(id, db)

    try:
        return patch_alert_rule(id, rule_data, db)
    except:
        # we reach here mostly because of Unique constraint violation,
        # other exceptions are not handled.
        raise HTTPException(
            status_code=400,
            detail="can't update Alert rule, there is a rule with the same symbol and price.",
        )
