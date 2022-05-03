import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase
from sqlalchemy import orm
import datetime


class User(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True, unique=True)
    login = sqlalchemy.Column(sqlalchemy.String, nullable=False, unique=True)
    password = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=False)


class Recipes(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'recipes'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True, unique=True)
    userID = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))
    user = orm.relation('User')


class Recipe(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'recipe'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           sqlalchemy.ForeignKey("users.id"), primary_key=True)
    time = created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                            default=datetime.datetime.now)
    cooktime = (sqlalchemy.Column(sqlalchemy.Integer))
    ingredients = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    photos = sqlalchemy.Column(sqlalchemy.String)
    steps = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    subcatID = sqlalchemy.Column(sqlalchemy.Integer,
                                 sqlalchemy.ForeignKey("categories.subcatID"),
                                 nullable=False)


class ProductCards(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'product-cards'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           sqlalchemy.ForeignKey("users.id"), primary_key=True)
    DishName = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    RatingSum = sqlalchemy.Column(sqlalchemy.Integer)
    reviews = sqlalchemy.Column(sqlalchemy.Integer)
    photo = sqlalchemy.Column(sqlalchemy.String)
    description = sqlalchemy.Column(sqlalchemy.String)


class Categories(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'categories'
    catID = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                              nullable=False)
    subcatID = sqlalchemy.Column(sqlalchemy.Integer)
    CatName = sqlalchemy.Column(sqlalchemy.String)


class Associations(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'associations'
    recepID = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("recipes.id"),
                                primary_key=True)
    word = sqlalchemy.Column(sqlalchemy.String)