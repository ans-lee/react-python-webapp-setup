import datetime
from typing import Tuple

from api.model import db
from api.model.user import User

def create_user(username: str, password: str, email: str) -> Tuple[bool, str]:
    query_username = User.query.filter_by(username=username).first()
    query_email = User.query.filter_by(email=email).first()
    if not query_username and not query_email:
        new_user = User(
            username=username,
            password=password,
            email=email,
            registered_on=datetime.datetime.utcnow()
        )
        db.session.add(new_user)
        db.session.commit()
        return True, 'Registered successfully!'
    elif query_username and query_email:
        return False, 'A user with the same username and email exists.'
    elif query_username:
        return False, 'A user with the same username exists.'
    return False, 'A user with the same email exists.'
