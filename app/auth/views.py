from flask import render_template,redirect,url_for
from . import auth
from ..models import User,Pitch
from .forms import LoginForm,RegistrationForm
from flask_login import login_user,logout_user,login_required
from werkzeug.security import check_password_hash, generate_password_hash
from .. import db
# from ..email import mail_message


@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username = login_form.email.data).first()
        if check_password_hash(user.password, form.password.data):
            login_user(user)
        return redirect(url_for('auth.pitches'))

        flash('Invalid username or Password')

    title = "login"
    return render_template('/login.html',login_form = login_form,title=title)
@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        email = form.email.data
        password = form.password.data

        hashed_password = generate_password_hash(password, method="sha256")
        new_user = User(first_name = first_name, 
                        last_name = last_name, 
                        username = username,  
                        email = email, 
                        password = hashed_password)
        db.session.add(new_user)
        db.session.commit()

        mail_message("Welcome to Pitchapp","email/welcome_user",user.email,user=user)

        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',registration_form = form)
@auth.route('/pitches', methods = ['GET', 'POST'])
@login_required
def pitches():
    pitches = Pitch.query.all()

    form = PitchForm()

    if form.validate_on_submit():
        author = form.author.data
        description= form.description.data

        schedule = Schedule(author=author, description = description)

        # add data to db
        db.session.add(pitch)
        db.session.commit()
        
        return redirect(url_for('pitches'))

    return render_template('pitch.html', form=form, name=current_user.username, pitches=pitches)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

if __name__ == '__main__':
    app.run(debug=True)