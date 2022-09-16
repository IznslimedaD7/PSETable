from app import app, login_manager
from flask import request, render_template, redirect, url_for
from models import Elements, db, Users
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_required, login_user, current_user, logout_user

@app.route('/main')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create-element', methods=['POST', 'GET'])
@login_required
def create():
    if request.method == 'POST':
        elem = Elements(title=request.form['title'], name=request.form['name'], body=request.form.get('ckeditor'))
        try:
            db.session.add(elem)
            db.session.commit()
            return redirect('/')
        except:
            db.session.rollback()
            print('ERROR')
    return render_template('create.html')

@app.route('/<name>')
def element(name):
    table_elem = Elements.query.filter_by(name=name).first_or_404()
    print(name, table_elem)
    return render_template('element.html', table_elem=table_elem)

@app.route('/<name>/redact', methods=['POST', 'GET'])
@login_required
def redact(name):
    table_elem = Elements.query.filter_by(name=name).first_or_404()
    if request.method == 'POST':
        table_elem.body = request.form.get('ckeditor')
        table_elem.title = request.form.get('title')
        try:
            db.session.commit()
            return redirect('/main')
        except:
            db.session.rollback()
            print('ERROR while trying redact')
    else:
        return render_template('redact.html', table_elem=table_elem)

@app.route('/reg', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        user = Users(nickname=request.form['nickname'], password=generate_password_hash(request.form['password']))
        try:
            db.session.add(user)
            db.session.commit()
            return redirect('/main')
        except:
            db.session.rollback()
            print('ERROR AFTER REGISTRATION')
    else:
        return render_template('registration.html')

@app.route('/login', methods=['POST', 'GET'])
def login_post():
    if current_user.is_authenticated:
        return redirect('/profile')

    if request.method == 'POST':
        nickname = request.form['nickname']
        password = generate_password_hash(request.form['password'])
        user = db.session.query(Users).filter(Users.nickname == nickname).first()
        print(user.password)
        if not user and not check_password_hash(password, user.password):
            #please help me 2x
            redirect('/login')
        else:
            login_user(user)
            return redirect('/profile')
        return redirect('/main')
    return render_template('login.html')


@app.route('/profile')
@login_required
def user_view():
    return render_template('profile.html')

@login_manager.user_loader
def load_user(user_id):
    return db.session.query(Users).get(user_id)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/main')

