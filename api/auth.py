from flask import Blueprint, render_template 
#import peewee as pw
#import database as db

auth_api = Blueprint('auth_api', __name__)

@auth_api.route('/auth', methods=['GET'])
def auth():
    return render_template('auth.html')
    
@auth_api.route('/auth', methods=['POST'])
def auth_post():
    return render_template('account_summary.html')