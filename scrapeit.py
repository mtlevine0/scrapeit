from flask import Flask, send_from_directory
from api import auth, account, auth_decorator
import os
import properties

app = Flask(__name__)

@app.route("/")
def main():
    return send_from_directory("static/", "index.html")

PORT = int(os.getenv('PORT', properties.d["port"]))

if __name__ == '__main__':
    
    app.register_blueprint(auth.auth_api)
    app.register_blueprint(account.account_api)
    app.run(debug=properties.d["debug"], host=properties.d["host"], port=PORT)