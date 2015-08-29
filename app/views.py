from app import app, lm, db
from flask import render_template, request, redirect, url_for, session, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from .forms import ImportanceForm, LoginForm
from .models import User, Laptop
from .auth import authenticate
from .log import Logger

logger = Logger()
logger.setLevel(logger.info)

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user

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
        return render_template('budget.html', extra_css=['budget'])
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
@login_required
def admin():
    logger.log('Current user:'+str(g.user))
    if g.user.is_authenticated():
        return redirect(url_for('laptops'))
    return redirect(url_for('login'))

@app.route('/admin/laptops')
@login_required
def laptops():
    return render_template('laptops.html', user=g.user, extra_css=[])

@app.route('/admin/stats')
@login_required
def stats():
    return render_template('stats.html', user=g.user, extra_css=[])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        logger.log('Redirecting...')
        return redirect(url_for('admin'))
    form = LoginForm()
    if form.validate_on_submit():
        logger.log('Form validation requested.')
        session['remember_me'] = form.remember_me.data
        remember_me = False
        if 'remember_me' in session:
            remember_me = session['remember_me']
            session.pop('remember_me', None)
        user = authenticate(form.user.data, form.password.data)
        if user:
            login_user(user, remember=remember_me)
            logger.log('Login succesful')
            logger.log('User: '+str(g.user))
            return redirect(url_for('laptops'))
        else:
            logger.log('Authentication failed')
            return redirect(url_for('login'))
    return render_template('login.html', form=form, extra_css=['login'])

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

'''@app.route('/post', methods=['GET', 'POST'])
def post():
	return request.form['budget']
'''
