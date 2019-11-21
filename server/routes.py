from flask import render_template, redirect
from server import app, db
from server.forms import DataForm
from server.models import Data

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test')
def test():
    data = Data.query.all()
    return render_template('test.html', data=data)


@app.route('/add_data', methods=['GET', 'POST'])
def add_data():
    form = DataForm()
    if form.validate_on_submit():
        print(form.text.data)
        data = Data(text=form.text.data)
        db.session.add(data)
        db.session.commit()
        return redirect('/test')
    return render_template('add_data.html', form=form)
