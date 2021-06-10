from flask_wtf import FlaskForm # will help us create form
from wtforms import StringField, TextAreaField, SubmitField # will help in creation of respective textfields
from wtforms.validators import Required # ensures that the fields are filled

class ReviewForm(FlaskForm):
  title = StringField('Review title', validators=[Required()]) # 2 para 1st = label 2nd = list of validtors
  review = TextAreaField('Movie review')
  submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
  bio = TextAreaField('Tell us about you.',validators = [Required()])
  submit = SubmitField('Submit')