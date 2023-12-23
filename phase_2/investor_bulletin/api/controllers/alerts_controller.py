from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.models import get_db
from resources.alert.alert_schema import Alert
from resources.alert.alert_service import get_all_alerts

router = APIRouter()


# Get all
@router.get("/", response_model=list[Alert])
def get_all_alerts_route(db: Session = Depends(get_db)):
    return get_all_alerts(db)
