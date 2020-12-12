from flask import request, session

def verify_role(fn):
    def wrap():
        session.permanent = True
        
        return fn()
    return wrap