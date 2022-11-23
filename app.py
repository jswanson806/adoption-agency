from flask import Flask, request, render_template, redirect, flash, session
from models import db,  connect_db, Pet
from forms import AddPetForm
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "itsasecret!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def list_pets():
    """Renders a list of all pets in the db."""
    pets = Pet.query.all()

    return render_template('base.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pets_form():
    """Renders AddPetForm."""

    form = AddPetForm()

    # if the form validates, add the pet to the database, commit, and redirect to the homepage 
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.age.data
        pet = Pet(name=name, 
                    species=species, 
                    photo_url=photo_url, 
                    age=age, 
                    notes=notes)

        db.session.add(pet)
        db.session.commit()

        return redirect('/')
    # if the form does not validate, render the form again
    else:
        return render_template('add_new_pet_form.html', form=form)


@app.route('/details/<int:pet_id>')
def show_pet_details(pet_id):
    """Renders details of specific pet."""
    pet = Pet.query.get_or_404(pet_id)

    return render_template('pet_details.html', pet=pet)


@app.route('/details/<int:pet_id>/edit', methods=["GET", "POST"])
def edit_pet_details(pet_id):
    """Renders edit form for specific pet."""
    pet = Pet.query.get_or_404(pet_id)

    # populate the form with existing information from the db
    form = AddPetForm(obj=pet)

    # if the form validates, edit the pet in the db, commit, and redirect to the pet details
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data

        db.session.commit()
        return redirect(f'/details/{pet.id}')
    # if the form does not validate, render the form again
    else:
        return render_template('edit_pet_form.html', form=form)

