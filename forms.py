from wtforms import StringField
from wtforms.validators import DataRequired
from flask_wtf import Form

class MyForm(Form):
    text = StringField('text', validators = [DataRequired()])
    
