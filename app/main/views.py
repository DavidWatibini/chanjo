from flask import render_template
from . import main
from .. import db

@main.route('/')
def index():

    title = 'Home - Welcome To Chanjo'

    return render_template('index.html', title = title)
