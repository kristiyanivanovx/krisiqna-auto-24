from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField, TextField, validators, ValidationError


class ContactForm(FlaskForm):
    name = TextField("Име", [validators.DataRequired("Моля, въведете вашето име.")])
    email = TextField("E-mail адрес", [validators.DataRequired("Моля, въведете вашия имейл адрес."),
                                       validators.Email("Моля, въведете вашия имейл адрес.")])
    subject = TextField("Тема", [validators.DataRequired("Моля, въведете тема.")])
    message = TextAreaField("Съобщение", [validators.DataRequired("Моля, въведете съобщение.")])
    submit = SubmitField("Изпрати")
