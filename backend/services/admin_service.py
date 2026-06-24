from backend.repositories.user_repository import (
    get_all_users
)

def fetch_all_users(db):

    return get_all_users(db)