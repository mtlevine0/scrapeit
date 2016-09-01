from flask import Blueprint, request, Response, jsonify
from flask import render_template, url_for, redirect, send_from_directory
import json
import database as db
from api import auth_decorator
from scrape import account_model


account_api = Blueprint('account_api', __name__)


#account summary 
@auth_decorator.login_required
@account_api.route('/api/account', methods=['GET'])
def account():
    
    
    return render_template('summary.html')


#account settings
@auth_decorator.login_required
@account_api.route('/api/account/settings', methods=['GET','POST'])
def settings():
    
    return render_template('settings.html')
    
    
#information on a specific scrape
@auth_decorator.login_required
@account_api.route('/api/account/scrape/<scrape_id>', methods=['GET'])
def get_scrape(scrape_id):
    
    return render_template('scrape.html')
    

#publish new scrape 
@auth_decorator.login_required
@account_api.route('/api/account/scrape/create', methods=['POST'])
def create_scrape():
    
    requestObj = request.get_json()
    responseObj= {}
    
    uid = requestObj['uid']
    name = requestObj['name']
    
    db.Scrape.add(uid=uid, name=name)
    
    responseObj['success'] = 'created scrape ' + name
    
    return jsonify(responseObj)
    
    
#edit params, delete scrape 
@auth_decorator.login_required
@account_api.route('/api/account/scrape/edit', methods=['POST'])
def edit_scrape(uid):
    
    return render_template('account_summary.html')