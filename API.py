from flask import Blueprint, jsonify, request
from data import db_session
from data.FoodFetish import User, Recipe
from werkzeug.security import generate_password_hash
from os import path

db_session.global_init('db/foodfetish.db')


blueprint = Blueprint(
    'food_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/recipes')
def get_news():
    db_sess = db_session.create_session()
    recepts = db_sess.query(Recipe).all()
    return jsonify(
        {
            'recipes':
                [item.to_dict()
                 for item in recepts]
        }
    )


# [item.to_dict(only=('id', 'userID', 'DishName',
#                     'cooktime', 'photo', 'description', 'CatName'))


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


@blueprint.route('/api/create/recipe', methods=['POST'])
def create_recipe():
    print(request.json)
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['name', 'time', 'descr', 'ingridients', 'steps', 'id']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    recipe = Recipe()
    recipe.id = request.json['id']
    recipe.userID = request.json['userID']
    recipe.DishName = request.json['name']
    recipe.cooktime = request.json['time']
    recipe.ingredients = 'да'
    db_sess.add(recipe)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/create/recipe/addphoto', methods=['POST'])
def check():
    print(request.files)
    file = request.files['upload_file']
    file.sve(path.join('static', file.filename))
    return jsonify({'success': 'OK'})