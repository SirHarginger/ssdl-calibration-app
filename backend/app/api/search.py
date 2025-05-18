from fastapi import APIRouter, Depends
from ...services.search_index import search_calibrations
from sqlalchemy.orm import Session
from ...database.db import get_db
from fastapi_users import FastAPIUsers
from ...models.user import User
from ...utils.auth import auth_backend, user_manager

router = APIRouter(prefix="/search", tags=["search"])

fastapi_users = FastAPIUsers[User, int](user_manager, [auth_backend])
current_user = fastapi_users.current_user()

@router.get("/")
def search(
    query: str,
    year: int = None,
    company: str = None,
    unit: str = None,
    db: Session = Depends(get_db),
    user: User = Depends(current_user)
):
    results = search_calibrations(query, year, company, unit, db)
    return {"results": results}