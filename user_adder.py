from flask import Flask
from data import db_session
from data.FoodFetish import User, Recipes, Recipe, Categories, Associations
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def finished(bol):
    if bol == 0:
        return 'Is not finished'
    return 'Is finished'


def main():
    db_session.global_init('db/foodfetish.db')
    db_sess = db_session.create_session()
    user = User()
    user.login = 'admin'
    user.password = generate_password_hash('admin')
    user.email = 'pppoz22@gmal.com'
    user.name = 'Капитан Крюк'
    db_sess.add(user)
    db_sess.commit()


    a = ['Preparations' ,'PastriesDesserts', 'MainDishes', 'Breakfasts',
         'Salads', 'Soups', 'PastaPizza', 'Snacks', 'Sandwiches', 'Risotto',
         'Drinks', 'SaucesMarinades', 'Broths']
    for i in a:
        rec = Categories()
        rec.CatName = i
        db_sess.add(rec)
        db_sess.commit()
    # recepts = db_sess.query(User).all()
    # print(recepts)
        # db_session.global_init(input())
        # db = db_session.create_session()
        #
        # jobs = [job for job in db.query(Jobs)]
        # filtered_jobs = list()
        # for i in jobs:
        #     if not i.is_finished and i.work_size < 20:
        #         filtered_jobs.append(f'<Job> {i.job}')
        # print(*filtered_jobs, sep='\n')


if __name__ == '__main__':
    main()