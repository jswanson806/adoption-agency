from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import NumberRange, InputRequired, Optional, URL

pet_types = ["dog", "cat", "porcupine"]

class AddPetForm(FlaskForm):
    """Form for adding pets.
    
    >>>  name = StringField("Pet Name", validators=[InputRequired(message="Please enter a name")])
    >>> species = StringField("Species", validators=[InputRequired(message="Please enter a species")])
    >>> photo_url = StringField("Image URL", validators=[URL(require_tld=False, message="Please enter a valid URL"), Optional()])
    >>> age = IntegerField("Age", validators=[NumberRange(min=0, max=30, message="Please enter value between 0 and 30"), Optional()])
    >>> notes = StringField("Notes", validators=[Optional()])

    """

    name = StringField("Pet Name", validators=[InputRequired(message="Please enter a name")])
    species = StringField("Species", validators=[InputRequired(message="Please enter a species")])
    photo_url = StringField("Image URL", validators=[URL(require_tld=False, message="Please enter a valid URL"), Optional()])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30, message="Please enter value between 0 and 30"), Optional()])
    notes = StringField("Notes", validators=[Optional()])