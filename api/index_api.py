from flask import Blueprint, render_template

index_api = Blueprint('index_api', __name__)

@index_api.route('/', methods=['GET'])
def index():
    return render_template('index.html')