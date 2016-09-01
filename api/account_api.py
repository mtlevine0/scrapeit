from flask import Blueprint, render_template

from api import auth_decorator

account_api = Blueprint('account_api', __name__)

@account_api.route('/account', methods=['GET'])
@auth_decorator.login_required
def account():
    return render_template('summary.html')
    
@account_api.route('/account/settings', methods=['GET','POST'])
def settings():
    return render_template('settings.html')

@account_api.route('/account/scrape/new', methods=['GET'])
def new_scrape():
    return render_template('scrape.html')

@account_api.route('/account/scrape/create', methods=['POST'])
def create_scrape():
    return render_template('account_summary.html')
    
@account_api.route('/account/scrape/edit', methods=['POST'])
def edit_scrape():
    return render_template('account_summary.html')