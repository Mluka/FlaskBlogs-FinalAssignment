#-*-coding:utf-8-*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(FlaskForm):
    email = StringField(u'邮箱', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField(u'密码', validators=[Required()])
    remember_me = BooleanField(u'保持登陆')
    submit = SubmitField(u'登陆')

class RegistrationForm(FlaskForm):
    email = StringField(u'邮箱', validators=[Required(), Length(1, 64),
                                             Email()])
    username = StringField(u'用户名', validators=[Required(), Length(1, 64)])
    password = PasswordField(u'密码', validators=[Required(),
                EqualTo('password2', message=u'密码必须相同。')])
    password2 = PasswordField(u'确认密码', validators=[Required()])
    submit = SubmitField(u'注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(u'邮箱已经被注册')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(u'用户名已经被注册')

class ChangePasswordForm(FlaskForm):
    old_password = PasswordField(u"旧密码", validators=[Required()])
    password = PasswordField(u"新密码", validators=[
                Required(), EqualTo('password2', message=u'密码必须相同。')])
    password2 = PasswordField(u"确认新密码", validators=[Required()])
    submit = SubmitField(u'确认更改')

class PasswordResetRequestForm(FlaskForm):
    email = StringField(u'邮箱', validators=[Required(), Length(1, 64),
                                             Email()])
    submit = SubmitField(u'重置密码')

class PasswordResetForm(FlaskForm):
    email = StringField(u'邮箱', validators=[Required(), Length(1, 64),
                                            Email()])
    password = PasswordField(u'新密码', validators=[
        Required(), EqualTo('password2', message=u'密码必须相同')])
    password2 = PasswordField(u'确认密码', validators=[Required()])
    submit = SubmitField(u'重置密码')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is None:
            raise ValidationError(u'未知邮箱地址')

class ChangeEmailForm(FlaskForm):
    email = StringField(u'新邮箱', validators=[Required(), Length(1, 64),
                                                 Email()])
    password = PasswordField(u'密码', validators=[Required()])
    submit = SubmitField(u'更新邮箱地址')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(u'邮件已经被注册')