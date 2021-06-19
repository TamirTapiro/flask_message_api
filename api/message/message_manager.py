from pymongo.collection import ReturnDocument
from models.Entities import Message, messages_collection
import pymongo
from flask import Blueprint,request, session
import json
from bson import json_util

message_manager_blueprint = Blueprint('message_manager','message_manager_blueprint')

def get_user_id():
    return session['user']['id']

def get_messages(filters):
    print(type(filters))
    results = {'user_id': session['user']['id']}
    try:
        results['messages'] = list(messages_collection.find(filters, {'_id': False}))
        print(results)
        if results is not None:
            return json.dumps(results, default=json_util.default)
        else:
            raise 
    except:
        return json.loads({'statusCode': 404, 'message': 'some error eccured.'})

@message_manager_blueprint.before_request
def before_request_callback():
        if not 'user' in session:
            return {'message': 'You must login before use this API.'}, 404
        # else:
        #     session['user'] = session['user'] #refresh


@message_manager_blueprint.route('/write_message', methods=['POST'])
def write_message():
    try:
        msg = Message(request.get_json())
    except:
        return {'message': 'Message must have a receiver field.'}, 203
    msg.sender = get_user_id()
    messages_collection.insert_one(msg.__dict__)
    return {'info': 'message has been sent'}, 200

@message_manager_blueprint.route('/')
def get_all_messages():
    filters = {"$or": [{'sender': get_user_id()}, {'receiver': get_user_id()}]}
    return get_messages(filters)

@message_manager_blueprint.route('/incoming')
def get_incoming_messages():
    filters =  {'receiver': get_user_id()}
    return get_messages(filters)

@message_manager_blueprint.route('/outgoing')
def get_outgoing_messages():
    filters = {'sender': get_user_id()}
    return get_messages(filters)

@message_manager_blueprint.route('/unread')
def get_unread_messages():
    filters = {"$and": [{'receiver': get_user_id()}, {'has_read': False}]}
    return get_messages(filters)

# returns the newest message only
@message_manager_blueprint.route('/read_message')
def read_message():
    filters = {"$and": [{'receiver': get_user_id()}, {'has_read': False}]} 
    results = {'user_id': get_user_id()}
    print(filters)
    try:
        results['message'] = messages_collection.find_one_and_update(filters,
            {'$set': {'has_read': True}},
            {'_id': False},
            sort=[('_id', pymongo.DESCENDING)])
        print(results)
        if results is not None:
            return json.dumps(results, default=json_util.default)
        else:
            raise 
    except:
        return json.dumps({'message': 'some error eccured.'}, default=json_util.default), 404
    
@message_manager_blueprint.route('/delete/<which_one>')
def delete_message(which_one):
    if which_one.lower() == 'newest':
        msg = messages_collection.find_one_and_delete({"$or": [{'receiver': get_user_id()}, {'sender': get_user_id()}]}, 
            sort=[('_id', pymongo.DESCENDING)])
        return json.dumps(msg, default=json_util.default), 200
    
    elif which_one.lower() == 'oldest':
        msg = messages_collection.find_one_and_delete({"$or": [{'receiver': get_user_id()}, {'sender': get_user_id()}]},
         sort=[('_id', pymongo.ASCENDING)])
        return json.dumps(msg, default=json_util.default), 200
    
    return json.dumps({'message': 'some error eccured.'}, default=json_util.default), 404