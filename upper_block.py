from flask import Flask
from flask import url_for, request, render_template
from flask_login import LoginManager
from data.FoodFetish import User
from data import db_session
from data import API



def main():
    db_session.global_init("db/foodfetish.db")
    app.register_blueprint(API.blueprint)
    app.run(port=8080, host='127.0.0.1')


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/site')
def eat():
    return render_template('main_win.html')


if __name__ == '__main__':
    main()