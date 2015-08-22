from app import app
from flask import render_template, request, redirect, url_for, session
from .forms import ImportanceForm, LoginForm


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
        return render_template('budget.html', extra_css=[])
    return redirect(url_for('options'))


@app.route('/options', methods=['GET', 'POST'])
def options():
    if 'budget' in session:
        form = ImportanceForm()
        if form.validate_on_submit():
            data = session['budget'] + "e, "
            for field in form:
                data += str(field.data) + "<br>"
            return data
        return render_template('options.html', form=form, budget=session['budget'], extra_css=[])
    return redirect(url_for('budget'))

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    form = LoginForm()
    if form.validate_on_submit():
        if form.user.data == 'TimoJarv' and form.passwd.data == 'pass':
            return 'Hello!'
        return 'Wrong login!'
    return render_template('login.html', form=form, extra_css=['login'])

'''@app.route('/post', methods=['GET', 'POST'])
def post():
	return request.form['budget']
'''
