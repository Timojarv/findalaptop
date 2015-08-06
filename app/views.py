from app import app
from flask import render_template
from .forms import TestForm


@app.route('/')
@app.route('/index')
def index():
	form = TestForm()
	return render_template('index.html', form = form)
