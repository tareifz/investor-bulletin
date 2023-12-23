from api.controllers.market_controllers import router as MarketRouter
from api.controllers.rules_controller import router as AlertRuleRouter
from api.controllers.alerts_controller import router as AlertRouter


def init_routes(app):
    app.include_router(MarketRouter, prefix="/market-prices", tags=["Market"])
    app.include_router(AlertRuleRouter, prefix="/alert-rules", tags=["Rules"])
    app.include_router(AlertRouter, prefix="/alerts", tags=["Alert"])
    return app
