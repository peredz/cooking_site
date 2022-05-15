from requests import get, post
from flask import Flask, redirect
from flask import render_template, request
from flask_login import LoginManager, login_required, logout_user, login_user
from data.FoodFetish import User
from data import db_session
import api
from loginform import LoginForm, RegisterForm
from os import path
from werkzeug.security import generate_password_hash
from random import choice, randint


def main():
    db_session.global_init("db/foodfetish.db")
    app.register_blueprint(api.blueprint)
    app.run(port=8080, host='127.0.0.1')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if LoginForm.authorization_check(form, user):
            login_user(user, remember=form.remember_me.data)
            return redirect('/home')
        else:
            msg = 'Неверный логин или пароль'
    return render_template('login.html', title='Авторизация', form=form,
                           massage=msg)


@app.route('/site', methods=['POST', 'GET'])
def eat():
    if request.method == 'GET':
        return render_template('base.html')
    elif request.method == 'POST':
        pass


@app.route('/home')
def index():
    return render_template('main_menu.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/home")


@app.route('/profile/<us_id>', methods=['GET', 'POST'])
def profile(us_id):
    if request.method == 'GET':
        user_info = get(f'http://127.0.0.1:8080/api/user/{us_id}').json()
        return render_template('profile.html', name=user_info['user'][0]['name'],
                               ava=user_info['user'][0]['profile_photo'],
                               login=user_info['user'][0]['login'])
    elif request.method == 'POST':
        file = request.files['file']
        if file:
            filename, file_extension = path.splitext(file.filename)
            if file_extension in ['.jpg', '.png']:
                name = [choice([1, 2, 3, 4, 5, 6, 7, 8, 9,
                                'q', 'w', 'e', 'r', 't',
                                'y', 'u', 'i', 'o', 'p',
                                'a', 's', 'd', 'f', 'g',
                                'h', 'j', 'k', 'l', 'z',
                                'x', 'c', 'v', 'b', 'n',
                                'm']) for i in range(randint(6, 14))]
                file.save(path.join('static/images/profiles',
                                    f'{name}{file_extension}'))
            else:
                user_info = get(
                    f'http://127.0.0.1:8080/api/user/{us_id}').json()
                return render_template('profile.html',
                                       name=user_info['user'][0]['name'],
                                       ava=user_info['user'][0][
                                           'profile_photo'],
                                       login=user_info['user'][0]['login'],
                                       msg='Недопустимый формат файла')


@app.route('/check')
def check():
    file = {'upload_file': open('static/images/hand.png', 'rb')}
    post(f'http://127.0.0.1:8080/api/create/recipe/addphoto', files=file)
    return redirect("/home")


@app.route('/register', methods=['GET', 'POST'])
def reg():
    msg = ''
    form = RegisterForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = [i for i in db_sess.query(User).filter(User.email == form.email.data)]
        login = [i for i in db_sess.query(User).filter(User.login == form.login.data)]
        if len(user) == 0 and len(login) == 0:
            user = User()
            user.login = form.login.data
            user.password = generate_password_hash(form.password.data)
            user.email = form.email.data
            user.name = form.name.name
            db_sess.add(user)
            db_sess.commit()
            login_user(user, remember=form.remember_me.data)
            return redirect('/home')
        else:
            msg = 'Аккаунт с такой почтой или логином уже существует'
    return render_template('registr.html', title='Авторизация', form=form,
                           massage=msg)


@app.route('/create/rcp', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create_rcp.html')
    elif request.method == 'POST':
        vals = [i for i in list(request.form.listvalues()) if len(i) > 1]
        print(vals)
        dct = dict()
        ks = request.form.keys()
        print(ks)
        keyss = list()
        for i in ks:
            if i not in keyss:
                keyss.append(i)
        for i in keyss:
            if i == 'ingridients':
                word = request.form[i]
                vl = [i for i in vals if word in i]
                if len(vl) > 0:
                    vl = [i for i in vals if word in i][0]
                dct[i] = vl
            elif i == 'steps':
                word = request.form[i]
                vl = [i for i in vals if word in i]
                if len(vl) > 0:
                    vl = [i for i in vals if word in i][0]
                dct[i] = vl
            else:
                dct[i] = request.form[i]
        print(dct, sep='\n')
        # dct['id'] = user_id
        file = request.files['file']
        if file:
            filename, file_extension = path.splitext('/path/to/somefile.ext')
            if file_extension in ['jpg', 'png']:
                file.save(path.join('static/images', file.filename))
        post(f'http://127.0.0.1:8080/api/create/recipe/addphoto',
             json=dct)
        return redirect("/home")



if __name__ == '__main__':
    main()