from flask import Blueprint
forms = Blueprint('forms', __name__)

@auth.route('/login')
def login():
    return "<p>Login</p>"


@forms.route('/logout')
def logout():
    return "<h1> Logout <h1>"

@forms.route('/register')
def register():
    return "<h1> Register <h1>"