import json

from flask import Response, request
from functools import wraps
import jwt

import properties

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        responseObj = {}
        try:
            JWTBearer = request.headers.get('Authorization').split(' ')[1]
        except:
            responseObj['error'] = 'InvalidJWT'
            return Response(json.dumps(responseObj), status=403, mimetype='application/json')
        else:
            if JWTBearer:
                try:
                    responseObj = jwt.decode(JWTBearer, properties.d['JWTSecret'], audience='ide.c9.io', issuer='scrapeit')
                except jwt.InvalidIssuedAtError:
                    responseObj['error'] = 'InvalidIssuedAtError'
                    return Response(json.dumps(responseObj), status=403, mimetype='application/json')
                except jwt.ExpiredSignatureError:
                    responseObj['error'] = 'ExpiredSignatureError'
                    return Response(json.dumps(responseObj), status=403, mimetype='application/json')
                except jwt.InvalidAudienceError:
                    responseObj['error'] = 'InvalidAudienceError'
                    return Response(json.dumps(responseObj), status=403, mimetype='application/json')
                except jwt.InvalidIssuerError:
                    responseObj['error'] = 'InvalidIssuerError'
                    return Response(json.dumps(responseObj), status=403, mimetype='application/json')
                except jwt.DecodeError:
                    responseObj['error'] = 'DecodeError'
                    return Response(json.dumps(responseObj), status=403, mimetype='application/json')
            else:
                responseObj['error'] = 'InvalidAuthorizationHeader'
                return Response(json.dumps(responseObj), status=403, mimetype='application/json')
                
            kwargs['JWT'] = responseObj
                
        return f(*args, **kwargs)
    return decorated_function
    
def register_validation(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        requestObj = request.get_json()
        responseObj = {}
        
        try:
            password = requestObj['password']
        except:
            responseObj['error'] = 'Invalid Registration Information'
            return Response(json.dumps(responseObj), status=500, mimetype='application/json')
        try:
            username = requestObj['username']
        except:
            responseObj['error'] = 'Invalid Registration Information'
            return Response(json.dumps(responseObj), status=500, mimetype='application/json')
        try:
            email = requestObj['email']
        except:
            responseObj['error'] = 'Invalid Registration Information'
            return Response(json.dumps(responseObj), status=500, mimetype='application/json')

        if len(password) < 9:
            responseObj['error'] = 'Invalid Password Length: Must be at least 8 characters.'
            return Response(json.dumps(responseObj), status=500, mimetype='application/json')
        if (len(username) < 5) or (len(username) >= 32):
            responseObj['error'] = 'Invalid Username Length: Must be between 5 and 32 characters.'
            return Response(json.dumps(responseObj), status=500, mimetype='application/json')
        
        return f(*args, **kwargs)
    return decorated_function
