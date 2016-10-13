import datetime
import json

from flask import Flask, Blueprint, request, Response, jsonify
import jwt

import database as db
import properties
from api import auth_decorator

auth_api = Blueprint('auth_api', __name__)

@auth_api.route('/api/auth/register', methods=['POST'])
@auth_decorator.register_validation
def register():
    requestObj = request.get_json()
    responseObj= {}
    password = requestObj['password']
    username = requestObj['username']
    email = requestObj['email']
    
    if not usernameAvailable(username):
        try:
            db.User.add(username=username, password=password, email=email)
            db.Role.grantRole(username=username, role='user')
        except:
            responseObj['error'] = 'failed to register user'
            return jsonify(responseObj)
        else:
            responseObj['jwt'] = generateJWT(username, 'user')
            responseObj['success'] = 'registered user'
            responseTest = Response(json.dumps(responseObj), status=200, mimetype='application/json')
            responseTest.set_cookie('jwt', responseObj['jwt'])
            return responseTest
        
    else:
        responseObj['error'] = "username not available"
        return jsonify(responseObj)
        
@auth_api.route('/api/auth/role', methods=['GET'])
@auth_decorator.login_required(['admin', 'moderator', 'user'])
def role(JWT):
    print("testing role endpoint")
    return jsonify(JWT)

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
            responseObj['jwt'] = generateJWT(username, 'user')
            responseObj['success'] = 'User Authentication Successful'
            responseTest = Response(json.dumps(responseObj), status=200, mimetype='application/json')
            responseTest.set_cookie('jwt', responseObj['jwt'])
            return responseTest
        else:
            responseObj['error'] = 'User Authentication Failed'
            return jsonify(responseObj)
            
@auth_api.route('/api/auth/refresh', methods=['POST'])
@auth_decorator.login_required(['admin', 'user'])
def refresh(JWT):
    responseObj = {}
    username = JWT['username']
    responseObj['jwt'] = generateJWT(username)
    responseObj['success'] = 'Token Refresh Successful'
    responseTest = Response(json.dumps(responseObj), status=200, mimetype='application/json')
    responseTest.set_cookie('jwt', responseObj['jwt'])
    return responseTest
    
@auth_api.route('/api/auth/private', methods=['GET'])
@auth_decorator.login_required(['moderator'])
def private(JWT):
    return jsonify(JWT['username'])
    
@auth_api.route('/api/auth/test', methods=['GET'])
@auth_decorator.login_required(['user'])
def test(JWT):
    return jsonify(JWT)
    
def generateJWT(username, role):
    JWT = {}
    JWT['iss'] = properties.d['JWTIss']
    JWT['iat'] = datetime.datetime.utcnow()
    JWT['exp'] = datetime.datetime.utcnow() + datetime.timedelta(seconds=int(properties.d['JWTTTL']))
    JWT['aud'] = properties.d['JWTAud']
    JWT['sub'] = properties.d['JWTSub']
    JWT['username'] = username
    JWT['role'] = role;
    JWTEncoded = jwt.encode(JWT, properties.d['JWTSecret'], algorithm=properties.d['JWTAlgo']).decode('utf-8')
    return JWTEncoded
    
def usernameAvailable(username):
    try:
        user = db.User.get(username=username)
    except:
        return False
    else:
        return True


