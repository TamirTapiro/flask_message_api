from flask import Flask, Blueprint, session, request
from api.message.message_manager import message_manager_blueprint
from api.user.user_manager import user_manager_blueprint
from models.Entities import messages_collection, users_collection
from bson.json_util import ObjectId
import json
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "MostSecretKeyInTheWorld"

# class MyEncoder(json.JSONEncoder):

#     def default(self, obj):
#         if isinstance(obj, ObjectId):
#             return str(obj)
#         return super(MyEncoder, self).default(obj)

# app.json_decoder = MyEncoder
app.register_blueprint(message_manager_blueprint, url_prefix="/api/messages")
app.register_blueprint(user_manager_blueprint, url_prefix='/api/auth')
app.permanent_session_lifetime = timedelta(minutes=60)


@app.errorhandler(404)
def request_not_found(e):
    return {'message': 'route not found'}, 404

if __name__ == '__main__':
    app.run(debug=True)
