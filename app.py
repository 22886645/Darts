from flask import Flask
app = Flask(__name__)
app.config['SECRET KEY'] = 'zfgb6554vddfgsrg54351f'

from .views import views
from .forms import forms

app.register_blueprint(views, url_prefix='/')
app.register_blueprint(forms, url_prefix ='/')
    
if __name__ == '__main__':
    app.run(debug=True)

