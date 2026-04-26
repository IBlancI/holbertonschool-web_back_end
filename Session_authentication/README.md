0x07. Session authentication

Simple API

Simple HTTP API for playing with User/User Session model.

models/

base.py: base of all models of the API - handle serialization to file
user.py: user model
user_session.py: user session model
api/v1

app.py: entry point of the API
views/index.py: basic endpoints of the API: /status and /stats
views/users.py: all users endpoints
views/session_auth.py: all types of authentication with sessions