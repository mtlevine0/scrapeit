import datetime

from flask import Flask, Blueprint, request, Response, jsonify
import jwt

import database as db
import properties
from api import auth_decorator

auth_api = Blueprint('auth_api', __name__)

@auth_api.route('/api/auth/register', methods=['POST'])
#@auth_decorator.register_validation
def register():
    requestObj = request.get_json()
    responseObj= {}
    password = requestObj['password']
    username = requestObj['username']
    email = requestObj['email']
    
    # db.User.add(username=username, password=password, email=email)
    # return "test"
    if not usernameAvailable(username):
        try:
            db.User.add(username=username, password=password, email=email)
        except:
            responseObj['error'] = 'failed to register user'
            return jsonify(responseObj)
        else:
            responseObj['jwt'] = generateJWT(username)
            responseObj['success'] = 'registered user'
            return jsonify(responseObj)
    else:
        responseObj['error'] = "username not available"
        return jsonify(responseObj)
    

@auth_api.route('/api/auth/login', methods=['POST'])
def login():
    requestObj = request.get_json()
    responseObj = {}
    username = requestObj['username']
    password = requestObj['password']
    try:
        user = db.User.get(username=username)
    except:
        responseObj['error'] = 'User Authentication Failed'
        return jsonify(responseObj)
    else:
        if user.checkPassword(password):
            responseObj['jwt'] = generateJWT(username)
            responseObj['success'] = 'User Authentication Successful'
            return jsonify(responseObj)
        else:
            responseObj['error'] = 'User Authentication Failed'
            return jsonify(responseObj)
            
@auth_api.route('/api/auth/refresh', methods=['POST'])
@auth_decorator.login_required
def refresh():
    responseObj = {}
    JWTBearer = request.headers.get('Authorization').split(' ')[1]
    incomingJWT = jwt.decode(JWTBearer, properties.d['JWTSecret'], audience=properties.d['JWTAud'], issuer=properties.d['JWTIss'])
    username = incomingJWT['username']
    responseObj['jwt'] = generateJWT(username)
    responseObj['success'] = 'Token Refresh Successful'
    return jsonify(responseObj)
    
@auth_api.route('/api/auth/private', methods=['GET'])
@auth_decorator.login_required
def private():
    JWTBearer = request.headers.get('Authorization').split(' ')[1]
    responseObj = {}
    try:
        responseObj = jwt.decode(JWTBearer, properties.d['JWTSecret'], audience=properties.d['JWTAud'], issuer=properties.d['JWTIss'])
    except:
        responseObj['error'] = 'User Authentication Failed'
        return jsonify(responseObj)
    return jsonify(responseObj['username'])
    
@auth_api.route('/api/auth/test', methods=['GET'])
@auth_decorator.login_required
def test():
    JWTBearer = request.headers.get('Authorization').split(' ')[1]
    responseObj = {}
    try:
        responseObj = jwt.decode(JWTBearer, properties.d['JWTSecret'], audience=properties.d['JWTAud'], issuer=properties.d['JWTIss'])
    except:
        pass
    return jsonify(responseObj)
    
def generateJWT(username):
    JWT = {}
    JWT['iss'] = properties.d['JWTIss']
    JWT['iat'] = datetime.datetime.utcnow()
    JWT['exp'] = datetime.datetime.utcnow() + datetime.timedelta(seconds=int(properties.d['JWTTTL']))
    JWT['aud'] = properties.d['JWTAud']
    JWT['sub'] = properties.d['JWTSub']
    JWT['username'] = username
    JWTEncoded = jwt.encode(JWT, properties.d['JWTSecret'], algorithm=properties.d['JWTAlgo']).decode('utf-8')
    return JWTEncoded
    
def usernameAvailable(username):
    try:
        user = db.User.get(username=username)
    except:
        return False
    else:
        return True


