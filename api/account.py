from flask import Blueprint, render_template

account_api = Blueprint('account_api', __name__)

@account_api.route('api/account', methods=['GET'])
def account(uid):
    return render_template('summary.html')
    
@account_api.route('api/account/settings', methods=['GET','POST'])
def settings(uid):
    return render_template('settings.html')

@account_api.route('api/account/scrape/new', methods=['GET'])
def new_scrape(uid):
    return render_template('scrape.html')

@account_api.route('api/account/scrape/create', methods=['POST'])
def create_scrape(uid):
    return render_template('account_summary.html')
    
@account_api.route('api/account/scrape/edit', methods=['POST'])
def edit_scrape(uid):
    return render_template('account_summary.html')