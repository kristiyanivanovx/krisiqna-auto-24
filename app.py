from flask import Flask, render_template, url_for, flash, request, redirect
from flask_wtf import FlaskForm
from forms import ContactForm
from flask_mail import Message, Mail
import os
import creds

# mail 

mail = Mail()

# app

app = Flask(__name__,
            static_url_path='',
            static_folder='web/static',
            template_folder='web/templates')

app.config['SECRET_KEY'] = creds.secret_key

# mail

# app.config["MAIL_SERVER"] = "smtp.mail.bg" # mail bg
# app.config["MAIL_PORT"] = 465 # mail bg

# app.config["MAIL_SERVER"] = "smtp.gmail.com" # Google
# app.config["MAIL_PORT"] = 587 # 465 for SSL - Google

# app.config["MAIL_SERVER"] = "appssmtp.abv.bg" # abv
# app.config["MAIL_PORT"] = 465 # 465 for SSL - abv

# elastic email

app.config["MAIL_SERVER"] = "smtp.elasticemail.com"
app.config["MAIL_PORT"] = 2525

app.config["MAIL_SUPPRESS_SEND"] = False
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USE_TLS"] = True

app.config["MAIL_USERNAME"] = creds.username
app.config["MAIL_PASSWORD"] = creds.password

mail.init_app(app)


# handle forms


@app.route('/contacts', methods=('GET', 'POST'))
def contacts():
    form = ContactForm()

    if request.method == 'POST':
        if not form.validate():
            flash('Моля, попълнете всички полета.')
            return render_template('contacts.html', form=form)
        else:
            msg = Message(form.subject.data, sender=creds.username, recipients=['georgi.asparuhov.2020@abv.bg'])
            msg.body = """От: %s \nE-mail: %s\nСъобщение: %s\nСайт: Крисияна Ауто 24 
            ------------------------------------------------------------------
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)

            return render_template("message_sent.html")

    elif request.method == 'GET':
        return render_template('contacts.html', form=form)


# handle 404 error


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# handle app routes/pages


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/history")
def history():
    return render_template("history.html")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/prices")
def prices():
    return render_template("prices.html")


@app.route("/terms_and_conditions")
def terms_and_conditions():
    return render_template("terms_and_conditions.html")


if __name__ == '__main__':
    app.run()
    # app.run(ssl_context='adhoc')
