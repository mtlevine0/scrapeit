import json

from flask import Response, request
from functools import wraps
import jwt

import properties

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        payload = {}
        try:
            JWTBearer = request.headers.get('Authorization').split(' ')[1]
        except:
            payload['error'] = 'InvalidJWT'
            resp = Response(json.dumps(payload), status=403, mimetype='application/json')
            return resp
        else:
            if JWTBearer:
                try:
                    payload = jwt.decode(JWTBearer, properties.d['JWTSecret'], audience='ide.c9.io', issuer='scrapeit')
                except jwt.InvalidIssuedAtError:
                    payload['error'] = 'InvalidIssuedAtError'
                    resp = Response(json.dumps(payload), status=403, mimetype='application/json')
                    return resp
                except jwt.ExpiredSignatureError:
                    payload['error'] = 'ExpiredSignatureError'
                    resp = Response(json.dumps(payload), status=403, mimetype='application/json')
                    return resp
                except jwt.InvalidAudienceError:
                    payload['error'] = 'InvalidAudienceError'
                    resp = Response(json.dumps(payload), status=403, mimetype='application/json')
                    return resp
                except jwt.InvalidIssuerError:
                    payload['error'] = 'InvalidIssuerError'
                    resp = Response(json.dumps(payload), status=403, mimetype='application/json')
                    return resp
                except jwt.DecodeError:
                    payload['error'] = 'DecodeError'
                    resp = Response(json.dumps(payload), status=403, mimetype='application/json')
                    return resp
            else:
                payload['error'] = 'InvalidAuthorizationHeader'
                resp = Response(json.dumps(payload), status=403, mimetype='application/json')
                return resp
        return f(*args, **kwargs)
    return decorated_function