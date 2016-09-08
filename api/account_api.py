from flask import Blueprint, request, Response, jsonify
from flask import render_template, url_for, redirect, send_from_directory
import json
import database as db
from api import auth_decorator
from scrape import account_model


account_api = Blueprint('account_api', __name__)


#account summary 
@account_api.route('/api/account', methods=['GET'])
@auth_decorator.login_required
def account(JWT):
    
    return render_template('summary.html')


#account settings

@account_api.route('/api/account/settings', methods=['GET','POST'])
@auth_decorator.login_required
def settings(JWT):
    
    return render_template('settings.html')
    
