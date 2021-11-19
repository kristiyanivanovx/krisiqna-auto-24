from flask import Flask, render_template, url_for, flash, request, redirect
from flask_wtf import FlaskForm
from forms import ContactForm
from flask_mail import Message, Mail
from dotenv import load_dotenv
import os

load_dotenv()

mail = Mail()

app = Flask(__name__,
            static_url_path='',
            static_folder='web/static',
            template_folder='web/templates')

app.config['SECRET_KEY'] = os.urandom(16)

app.config["MAIL_SERVER"] = os.getenv('MAIL_SERVER')
app.config["MAIL_PORT"] = os.getenv('MAIL_PORT')

app.config["MAIL_SUPPRESS_SEND"] = False
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USE_TLS"] = True

app.config["MAIL_USERNAME"] = os.getenv('ELASTIC_EMAIL_USERNAME')
app.config["MAIL_PASSWORD"] = os.getenv('ELASTIC_EMAIL_PASSWORD')

mail.init_app(app)


@app.route('/contacts', methods=('GET', 'POST'))
def contacts():
    form = ContactForm()

    if request.method == 'POST':
        if not form.validate():
            flash('Моля, попълнете всички полета.')
            return render_template('contacts.html', form=form)
        else:
            try:
                msg = Message(
                    form.subject.data,
                    sender=os.getenv('ELASTIC_EMAIL_USERNAME'),
                    recipients=[os.getenv('MAIL_RECIPIENT')])
                msg.body = """От: %s \nE-mail: %s\nСъобщение: %s\nСайт: Крисияна Ауто 24\n
                ------------------------------------------------------------------
                """ % (form.name.data, form.email.data, form.message.data)
                mail.send(msg)
            except Exception as e:
                print(e.message)

            return render_template("message_sent.html")

    elif request.method == 'GET':
        return render_template('contacts.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


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
#     app.run()
    app.run(debug=True)
#     app.run(ssl_context='adhoc')
