from flask import Flask,render_template,redirect,request,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from forms import RegisterationForm,LoginForm,updateprofileForm
from flask_bcrypt import Bcrypt
from flask_login import LoginManager,UserMixin,login_user,current_user,logout_user,login_required

app = Flask(__name__)
app.config['SECRET KEY'] = 'zfgb6554vddfgsrg54351f'
bcrypt = Bcrypt(app)

# ----------------------- routes
# main page
@app.route('/')
def intro():
    return render_template('intro.html')

# history page
@app.route('/history')
def history():
    return render_template('history.html')

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

