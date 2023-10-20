from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    name = StringField("Name", render_kw={'placeholder': 'Name'},
                       validators=[DataRequired("Please enter your name.")])
    email = StringField("Email", render_kw={'placeholder': 'Email'},
                        validators=[DataRequired("Please enter your email address."), Email()])
    subject = StringField("Subject", render_kw={'placeholder': 'Subject'},
                          validators=[DataRequired("Please enter a subject.")])
    message = TextAreaField("Message", render_kw={'placeholder': 'Message'},
                            validators=[DataRequired("Please enter a message.")])
    submit = SubmitField("Send")
