from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User, Detail
from .. import db
# from .forms import BookForm

@main.route('/')
def index():

    title = 'Home - Welcome To Chanjo'


    return render_template('index.html')
