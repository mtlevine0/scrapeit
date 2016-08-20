from flask import Blueprint, render_template

account_api = Blueprint('account_api', __name__)

@account_api.route('/<uid>', methods=['GET'])
def account(uid):
    return render_template('account_summary.html')