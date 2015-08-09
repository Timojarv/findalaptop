from app import app
from flask import render_template, request, redirect, url_for, session
from .forms import TestForm


@app.route('/')
@app.route('/index')
def index():
	if 'budget' in session:
		return redirect(url_for('options'))
	return redirect(url_for('budget'))

@app.route('/budget', methods=['GET', 'POST'])
def budget():
	try:
		session['budget'] = request.form['budget']
	except KeyError:
		return render_template('budget.html')
	return redirect(url_for('options'))

@app.route('/options')
def options():
	if 'budget' in session:
		form = TestForm()
		for field in form:
			print field.id
		return render_template('options.html', form=form, budget=session['budget'])
	return redirect(url_for('budget'))

'''@app.route('/post', methods=['GET', 'POST'])
def post():
	return request.form['budget']
'''
