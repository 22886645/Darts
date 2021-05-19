from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def intro ():
    return "<h1>New Intro<h1>"


