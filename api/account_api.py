from flask import Blueprint, request, Response, jsonify
from flask import render_template, url_for, redirect, send_from_directory
import json


from api import auth_decorator

account_api = Blueprint('account_api', __name__)


#Account Summary 
@account_api.route('api/account', methods=['GET'])
def account(uid):

    return render_template('summary.html')


#Account Settings    
@account_api.route('api/account/settings', methods=['GET','POST'])
def settings(uid):
    
    return render_template('settings.html')
    
    
#View Individual Scrape    
@account_api.route('api/account/scrape/<scrape_id>', methods=['GET'])
def get_scrape(scrape_id):
    
    return render_template('scrape.html')


#Create New Scrape
@account_api.route('api/account/scrape/new', methods=['GET'])
def new_scrape(uid):
    
    return render_template('scrape.html')


#Publish Scrape
@account_api.route('api/account/scrape/create', methods=['POST'])
def create_scrape(uid):
    
    return render_template('account_summary.html')
    
    
#Edit Scrape Parameters, Delete Scrape, etc.     
@account_api.route('api/account/scrape/edit', methods=['POST'])
def edit_scrape(uid):
    
    return render_template('account_summary.html')