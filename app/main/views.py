from flask import render_template,request,redirect,url_for
from . import main
from flask_login import login_required

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'PITCH APP'
   
    
    return render_template('index.html',title = title)
# @main.route('/login')
# def login():
# @main.route('/comment/new/<int:id>', methods = ['GET','POST'])
# @login_required
# def new_comment(id):
#     pass

    
