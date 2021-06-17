from flask import request, Blueprint

from api.controller import BASE_API_URL
from api.service.user import create_user

USER_BLUEPRINT = Blueprint('user', __name__)

@USER_BLUEPRINT.route(f'{BASE_API_URL}/create-user', methods=['POST'])
def new_user():
    payload = request.get_json()
    result = create_user(payload['username'], payload['password'], payload['email'])

    if result[0]:
        return { 'message': result[1] }, 201
    return { 'message': result[1] }, 409
