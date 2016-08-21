from flask import Flask, Blueprint, request, redirect, url_for, Response, send_from_directory, jsonify
import peewee as pw
import database as db
import jwt
import json
import properties
import datetime
import time

auth_api = Blueprint('auth_api', __name__)

@auth_api.route('/api/auth/register', methods=['POST'])
def register():
    request_data = request.get_json()
    payload = {}
    try:
        db.User.create(username=request_data['username'], password=request_data['password'])
    except:
        payload['error'] = 'failed to register user'
        return jsonify(payload)
    else:
        payload['success'] = 'registered user'
        return jsonify(payload)
    

@auth_api.route('/api/auth/login', methods=['POST'])
def auth():
    request_data = request.get_json()
    payload = {}
    responseObj = {}
    try:
        user = db.User.get(username=request_data['username'])
    except:
        responseObj['error'] = 'User Authentication Failed'
        return jsonify(responseObj)
    else:
        if user.password == request_data['password']:
            payload['iss'] = 'scrapeit'
            payload['iat'] = datetime.datetime.utcnow()
            payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(seconds=int(properties.d['JWTTTL']))
            payload['aud'] = 'ide.c9.io'
            payload['sub'] = 'Dev'
            payload['username'] = request_data["username"]
            encoded = jwt.encode(payload, properties.d['JWTSecret'], algorithm=properties.d['JWTAlgo'])
            responseObj['jwt'] = encoded
            responseObj['success'] = 'User Authentication Successful'
            return jsonify(responseObj)
        else:
            responseObj['error'] = 'User Authentication Failed'
            return jsonify(responseObj)
    
@auth_api.route('/api/auth/private', methods=['GET'])
def private():
    JWTBearer = request.headers.get('Authorization').split(' ')[1]
    payload = {}
    try:
        payload = jwt.decode(JWTBearer, properties.d['JWTSecret'], audience='ide.c9.io', issuer='scrapeit')
    except jwt.InvalidIssuedAtError:
        payload['error'] = 'InvalidIssuedAtError'
        resp = Response(json.dumps(payload), status=403, mimetype='application/json')
    except jwt.ExpiredSignatureError:
        payload['error'] = 'ExpiredSignatureError'
        resp = Response(json.dumps(payload), status=403, mimetype='application/json')
    except jwt.InvalidAudienceError:
        payload['error'] = 'InvalidAudienceError'
        resp = Response(json.dumps(payload), status=403, mimetype='application/json')
    except jwt.InvalidIssuerError:
        payload['error'] = 'InvalidIssuerError'
        resp = Response(json.dumps(payload), status=403, mimetype='application/json')
    else:
        resp = Response(json.dumps(payload), status=200, mimetype='application/json')
    
    return resp

# @auth_api.route('/auth', methods=['GET'])
# def auth():
#     return render_template('auth.html')
    
# @auth_api.route('/auth', methods=['POST'])
# def auth_post():
#     return render_template('account_summary.html')
