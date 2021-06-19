from models.Entities import users_collection
from flask import Blueprint, request, session

user_manager_blueprint = Blueprint('user_manager','user_manager_blueprint')


@user_manager_blueprint.route('/login', methods=['POST'])
def login():
    cred = request.get_json()
    if 'email' not in cred or 'password' not in cred:
        return "ERROR", 404
    user = users_collection.find_one({'$and': [{'email': cred['email']}, {'password': cred['password']}]}, {'_id': False})
    print(user)
    if user is not None:
        session['user'] = user
    return {'message': 'you are logged in as: {}.'.format(session['user']['email'])}, 200

@user_manager_blueprint.route('/logout')
def logout():
    if 'user' in session:
        res = {'message': '{} logged out.'.format(session['user']['email'])}
        session.pop('user', None)
        return res, 200
    else:
        return {'message': 'there is no logged in user.'}, 201
