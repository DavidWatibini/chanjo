from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User, Detail
from .. import db
from .forms import BookForm

@main.route('/')
def index():

    title = 'Home - Welcome To Chanjo'

    book_form = BookForm()
    if request.method == "POST":
        sms_message = request.form['smsMessage']
        phone_number = request.form['phoneNumber']

        print(sms_message)
        print(phone_number)

        response = sms.send(sms_message,[phone_number])
        print(response)

    return render_template('index.html', title = title,book_form=book_form)
