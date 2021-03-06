# 表单类，所有的表单都储存在这里
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()],description='用户名')
    password = PasswordField('密码', validators=[DataRequired()], description='密码')
    remember_me = BooleanField('记住密码')
    submit = SubmitField('登陆')
    StringField()


class SearchForm(FlaskForm):
    submit = SubmitField('查询')