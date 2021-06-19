from pymongo import MongoClient
from datetime import datetime
import uuid
import ssl
import json

mongo_uri = "mongodb+srv://GoFrance10:GoFrance10@mydb.bwvcm.mongodb.net/"
client = MongoClient(mongo_uri, ssl_cert_reqs=ssl.CERT_NONE)

mydb = client["message_db"]
messages_collection = mydb["messages"]
users_collection = mydb["users"]





# class User():
#     def __init__(self):
#         self.id = str(uuid.uuid4())
#         self.email = ""
#         self.password = ""
#         self.incoming_messages = []
#         self.outgoing_messages = []

class Message():
    def __init__(self, sender, receiver, subject="", body="", creation_date=datetime.now(), has_read= False):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.creation_date = creation_date
        self.has_read = has_read
    
    def __init__(self, j):
        self.__dict__ = j
        if "creation_date" not in self.__dict__:
            self.creation_date = datetime.now()
        if "has_read" not in self.__dict__:
            self.has_read = False
        if "subject" not in self.__dict__:
            self.subject = ""
        if "body" not in self.__dict__:
            self.body = ""
        if "receiver" not in self.__dict__:
            raise
        
        not_allowed = []
        for attr in self.__dict__:
            if attr not in ["sender", "receiver", "subject", "has_read", "creation_date"]:
                not_allowed.append(attr)
        for attr in not_allowed:
            del self.__dict__[attr]

























# db = SQLAlchemy()
# class User(db.Model):
#     id = db.Column(db.String(32), primary_key=True)
#     email = db.Column(db.String(64), unique=True, nullable=False)
#     password = db.Column(db.String(16), unique=False, nullable=False)
#     incoming_messages = relationship("Message", backref="message_sender", lazy=True, 
#         foreign_keys = 'message.c.sender_id')
#     outgoing_messages = relationship("Message", backref="message_receiver", lazy=True, 
#         foreign_keys = 'message.c.receiver_id')

# class Message(db.Model):
#     id = db.Column(db.String(32), primary_key=True)
#     sender_id = db.Column(db.String(32), db.ForeignKey('user.id'))
#     receiver_id = db.Column(db.String(32), db.ForeignKey('user.id'))
#     body = db.Column(db.String(4096))
#     subject = db.Column(db.String(256))
#     creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     message_read = db.Column(db.Boolean, nullable=False, default=False)