from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField, TextField, validators, ValidationError

class ContactForm(FlaskForm):
  name = TextField("Име",  [validators.Required("Моля, въведете вашето име.")])
  email = TextField("E-mail адрес",  [validators.Required("Моля, въведете вашия имейл адрес."), validators.Email("Моля, въведете вашия имейл адрес.")])
  subject = TextField("Тема",  [validators.Required("Моля, въведете тема.")])
  message = TextAreaField("Съобщение",  [validators.Required("Моля, въведете съобщение.")])
  submit = SubmitField("Изпрати")