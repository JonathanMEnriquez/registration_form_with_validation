from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASS_REGEX = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")
app = Flask(__name__)
app.secret_key = 'yek_repus'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def submit():
    error = False
    if len(request.form['email']) < 1 or len(request.form['first_name']) < 1 or len(request.form['last_name']) < 1 or len(request.form['pass']) < 1:
        flash('All fields required', 'error')
        error = True
    if not request.form['first_name'].isalpha() or not request.form['last_name'].isalpha():
        flash(u'First/Last name must not contain numbers or special characters', 'error')
        error = True
    if len(request.form['pass']) < 8:
        flash(u'Password must contain at least 9 characters', 'error')
        error = True
    if not PASS_REGEX.match(request.form['pass']):
        flash(u'Passwords must contain 1 uppercase, 1 lowercase and 1 number', 'error')
        error = True
    if not EMAIL_REGEX.match(request.form['email']):
        flash(u'Email address must be valid', 'error')
        error = True
    if request.form['pass'] != request.form['confirm_pass']:
        flash(u'Email addresses must match', 'error')
        error = True
    else:
        if error == True:
            return redirect('/')
        else:
            session['email'] = request.form['email']
            session['first_name'] = request.form['first_name']
            session['last_name'] = request.form['last_name']
            session['pass'] = request.form['pass']
            flash(u'Thank you for registering', 'success')
            return redirect('/')

    return redirect('/')

@app.route('/other')
def other():
    print "other"
    return redirect('/')

app.run(debug=True)