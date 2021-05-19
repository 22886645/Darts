from flask import Flask,render_template,redirect,request,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from forms import RegisterationForm,LoginForm,updateprofileForm
from flask_bcrypt import Bcrypt
from flask_login import LoginManager,UserMixin,login_user,current_user,logout_user,login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'zfgb6554vddfgsrg54351f' #for csrf token
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dart.db'  #name of db
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'First log in'

# this model is has no use
class Semigame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    User_id = db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)
    num = db.Column(db.Integer, nullable=True)
    date = db.Column(db.DateTime, default=datetime.now)
    def __repr__(self):
        return f'SemiGame({self.id} - {self.User_id}- {self.num}- {self.date})'

# storing the game results
class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    User_id = db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False) #creating a one to many relationship with foreign key
    score = db.Column(db.Integer, nullable=True)
    date = db.Column(db.DateTime, default=datetime.now)
    def __repr__(self):
        return f'Game({self.id} - {self.User_id} - {self.score} - {self.date})' 

# storing MCQ results 
class Queeze(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    User_idhe user details
class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now)
    queezes = db.relationship('Queeze',backref='player',lazy=True) # setting up a one to many relationship 
    games = db.relationship('Game',backref='player',lazy=True)  # setting up a one to many relationship 
    semigames = db.relationship('Semigame',backref='player',lazy=True)
    def __repr__(self):
        return f'User({self.id} - {self.username} - {self.email} - {self.password} - {self.date})'
        # return '<User %r>' % self.username    



# user page 
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

 = db.Column(db.Integer,db.ForeignKey('user.id') ,nullable=False) #creating a one to many relationship with foreign key
    score = db.Column(db.Integer, nullable=True)
    date = db.Column(db.DateTime, default=datetime.now)
    def __repr__(self):
        return f'Queeze({self.id} - {self.User_id} - {self.score} - {self.date})'

# storing the user details
class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now)
    queezes = db.relationship('Queeze',backref='player',lazy=True) # setting up a one to many relationship 
    games = db.relationship('Game',backref='player',lazy=True)  # setting up a one to many relationship 
    semigames = db.relationship('Semigame',backref='player',lazy=True)
    def __repr__(self):
        return f'User({self.id} - {self.username} - {self.email} - {self.password} - {self.date})'
        # return '<User %r>' % self.username    



# user page 
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# ----------------------- routes
# main page
@app.route('/')
def intro():
    return render_template('intro.html')

# history page
@app.route('/history')
def history():
    return render_template('history.html')

# game page
@app.route('/game')
@login_required  #log in is required to be able to see the viewing page
def game():
    return render_template('game.html')  

@app.route('/queeze')
@login_required
def queeze():
    return render_template('queeze.html')

# registering the user
@app.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterationForm()
    if request.method=="POST":
        # return redirect('/success')
        hashedpass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        us = User(username=form.username.data,email=form.email.data,password=hashedpass)
        db.session.add(us)
        db.session.commit()
        flash("Registeration completed")
        return redirect(url_for('intro'))
    # return redirect('/success')
    if request.method=='GET':
        return render_template('register.html' , form=form)



@app.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash("You have successfully exited")
    else:
        flash("You have not manage to enter")
    return redirect(url_for('intro'))


@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        flash("This has been entered before")
        return redirect(url_for('intro'))
    form = LoginForm()
    if request.method=="POST":#checking the method of sending details
        userr = User.query.filter_by(email=form.email.data).first()
        if userr and bcrypt.check_password_hash( userr.password ,form.password.data):
            login_user(userr,remember=form.remember.data)
            flash("You have entered successfully")  #presenting the message in the form of flash 
            return redirect(url_for('intro')) 
        else:
            flash("failed login")
            return redirect(url_for('intro'))
            

    if request.method=='GET':
        return render_template('login.html' , form=form)


    
if __name__ == '__main__':
    app.run(debug=True)

