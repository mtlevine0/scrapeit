from flask import Blueprint, request, Response, jsonify
from flask import render_template, url_for, redirect, send_from_directory
import json
import database as db
from api import auth_decorator


scrape_api = Blueprint('scrape_api', __name__)


@scrape_api.route('/api/scrape/create', methods=['POST'])
#@auth_decorator.login_required
def create_scrape():
    
    requestObj = request.get_json()
    responseObj= {}
    
    uid = requestObj['uid']
    name = requestObj['name']
    
    db.Scrape.add(uid=uid, name=name)
    
    responseObj['success'] = 'created scrape ' + name
    
    return jsonify(responseObj)
    

#information on a specific scrape
@scrape_api.route('/api/scrape/<scrape_id>', methods=['GET'])
@auth_decorator.login_required
def get_scrape(JWT, scrape_id):
    
    return render_template('scrape.html')


#edit params, delete scrape 
@scrape_api.route('/api/scrape/<scrape_id>/edit', methods=['POST'])
@auth_decorator.login_required
def edit_scrape(JWT, scrape_id):
    
    return render_template('account_summary.html')

