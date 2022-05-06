from flask_restful import reqparse, abort, Api, Resource
from flask import Blueprint, jsonify, request
from data import db_session
from data.FoodFetish import User, Recipes, Recipe,\
    ProductCards, Categories, Associations
db_session.global_init('db/foodfetish.db')


blueprint = Blueprint(
    'food_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/recipes')
def get_news():
    db_sess = db_session.create_session()
    recepts = db_sess.query(Recipes).all()
    return jsonify(
        {
            'recipes':
                [item.to_dict(only=('id', 'userID', 'user'))
                 for item in recepts]
        }
    )


@blueprint.route('/api/users')
def get_users():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return jsonify(
        {
            'users':
                [item.to_dict()
                 for item in users]
        }
    )


@blueprint.route('/api/user/<ac_id>')
def get_user(ac_id):
    db_sess = db_session.create_session()
    users = db_sess.query(User).filter(User.id == ac_id)
    return jsonify(
        {
            'user':
                [item.to_dict()
                 for item in users]
        }
    )


@blueprint.route('/api/create/account', methods=['POST'])
def create_user():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['login', 'password', 'email']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    user = User()
    user.login = request.json['login'],
    user.password = request.json['password'],
    user.email = request.json['email'],
    db_sess.add(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})
