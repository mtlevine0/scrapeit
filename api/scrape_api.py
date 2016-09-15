from flask import Blueprint, request, Response, jsonify
from flask import render_template, url_for, redirect, send_from_directory
import json
import database as db
from api import auth_decorator
from scrape import scrape_model

scrape_api = Blueprint('scrape_api', __name__)

@scrape_api.route('/api/scrape/create', methods=['POST'])
@auth_decorator.login_required
def create_scrape(JWT):
    
    requestObj = request.get_json()
    
    name = requestObj['name']

    return jsonify(scrape_model.create(JWT['uid'], name))
    

#information on a specific scrape
@scrape_api.route('/api/scrape/<scrape_id>', methods=['GET'])
@auth_decorator.login_required
def get_scrape(JWT, scrape_id):
    
    return scrape_model.read(JWT['uid'], scrape_id)


#edit params, delete scrape 
@scrape_api.route('/api/scrape/<scrape_id>/edit', methods=['POST'])
@auth_decorator.login_required
def edit_scrape(JWT, scrape_id):
    
    return render_template('account_summary.html')

