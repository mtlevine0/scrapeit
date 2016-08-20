import os
from flask import Flask
from api import auth, account, index, error

app = Flask(__name__, static_url_path='/static')

port = os.getenv('PORT', '5000')


if __name__ == '__main__':
    app.register_blueprint(auth.auth_api)
    app.register_blueprint(account.account_api)
    app.register_blueprint(index.index_api)
    
    app.run(host='0.0.0.0', port=int(port), threaded=True, debug=True)