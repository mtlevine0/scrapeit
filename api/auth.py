from flask import Flask, Blueprint, request, redirect, url_for, Response, send_from_directory
#import peewee as pw
#import database as db

auth_api = Blueprint('auth_api', __name__)

@auth_api.route('/api/auth', methods=['GET'])
def auth():
    return "Hello World!"