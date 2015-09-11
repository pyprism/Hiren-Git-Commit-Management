#https://api.github.com/users/pyprism/events?type
from flask import Flask, redirect
from flask import render_template
from flask_debugtoolbar import DebugToolbarExtension
from flask import request
from flask.ext.login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_user import login_required, UserManager, UserMixin, SQLAlchemyAdapter
from user_model import User
import github
import os
import json
app = Flask(__name__)

app.debug = os.environ.get('DEBUG', False)


with open('config.json') as f:
    json_data = json.load(f)

# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = json_data['secret_key']
app.config['USER_ENABLE_EMAIL'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///hiren_git.sqlite')
app.config['CSRF_ENABLED'] = True

db = SQLAlchemy(app)
# Create all database tables
db.create_all()
# Setup Flask-User
db_adapter = SQLAlchemyAdapter(db, User)        # Register the User model
user_manager = UserManager(db_adapter, app)     # Initialize Flask-User

toolbar = DebugToolbarExtension(app)

login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
def hiren():
    return render_template('login.html')


@app.route('/register')
def register():
    if request.method == 'POST':
        pass


@app.route('/auth')
def github_auth():
    return redirect(github.auth())

@app.route('/callback')
def redirect():
    return request.args.get('code')
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port)
