Message API with Flask Python

Description:
simple web-API for send / read / delete messages

base url: https://flaskmessageapi.herokuapp.com

API:
  Auth:
    if you using the app for the first time, you have to log in - 
    https://flaskmessageapi.herokuapp.com/api/auth/login - POST
    body:
    {
      "email": "tamir@gmail.com" / "snir@gmail.com",
      "password": "1234"
    }
    
    in order to log out or change user use logout - 
    https://flaskmessageapi.herokuapp.com/api/auth/logout - GET - no additional params
    
  Messages:
    "/" - GET - https://flaskmessageapi.herokuapp.com/api/messages
    get all messages for user
    
    "/incoming" - GET - https://flaskmessageapi.herokuapp.com/api/messages/incoming
    get all incoming messages for user
    
    "/outgoing" - GET - https://flaskmessageapi.herokuapp.com/api/messages/outgoing
    get all outgoing messages for user
    
    "/unread" - GET - https://flaskmessageapi.herokuapp.com/api/messages/unread
    get all unreadden messages for user
    
    "/read_message" - GET - https://flaskmessageapi.herokuapp.com/api/messages/read_message
    get the newest message received for the user
    
    "/write_message" - POST - https://flaskmessageapi.herokuapp.com/api/messages/write_message
    write single message for someone
    body:
    {
      "receiver": "111" / "222" //user_id
      "subject": String,
      "body": String
    }
    
    "/delete/<oldest/newest>" - GET - https://flaskmessageapi.herokuapp.com/api/messages/delete/<which_one>
    delete the oldest or the newest message
    
