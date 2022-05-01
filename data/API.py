from flask_restful import reqparse, abort, Api, Resource
from flask import Blueprint, jsonify
import db_session
from data.FoodFetish import User, Recipes, Recipe,\
    ProductCards, Categories, Associations


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


@blueprint.route('/api/recpt')
def get_news():
    return "Обработчик в news_api"
