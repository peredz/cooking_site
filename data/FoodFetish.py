import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase
from sqlalchemy import orm
import datetime
from flask_login import UserMixin


class User(SqlAlchemyBase, UserMixin, SerializerMixin):

    def __repr__(self):
        return f'<user> {self.id} {self.login} {self.password}; {self.created_date}; {self.email}'

    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True, unique=True)
    login = sqlalchemy.Column(sqlalchemy.String, nullable=False, unique=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    password = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=False)
    profile_photo = sqlalchemy.Column(sqlalchemy.String, nullable=True,
                                      default='/static/images/nophoto.jpg')


class Recipe(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'recipe'
    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True,
                           primary_key=True)
    userID = sqlalchemy.Column(sqlalchemy.Integer,
                               sqlalchemy.ForeignKey("users.id"))
    DishName = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    time = created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                            default=datetime.datetime.now)
    cooktime = (sqlalchemy.Column(sqlalchemy.String))
    ingredients = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    photo = sqlalchemy.Column(sqlalchemy.String)
    steps = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    CatName = sqlalchemy.Column(sqlalchemy.String)
    description = sqlalchemy.Column(sqlalchemy.String)