from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DecimalField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp
from flaskblog.models import User



class RegistrationForm (FlaskForm):
    nama = StringField('Nama', validators = [DataRequired(message = 'Masukan nama anda disini')])
    ktp = StringField('Nomor KTP', validators = [DataRequired(message = 'Masukan ktp anda disini'), Length(min = 16, max = 16, message = 'Masukan nomor ktp anda dengan benar'), Regexp('^[0-9]+$', message="Nomor KTP harus angka") ])
  
    nomor_hp = StringField('Nomor Handphone', validators = [DataRequired(message = 'Masukan nomor handphone anda disini'), Regexp('^[0-9]+$', message="Nomor HP harus angka")])
    umur = StringField('Umur', validators = [DataRequired(message = 'Masukan umur anda disini'), Regexp('^[0-9]+$', message="Umur harus angka"),Length(min = 0, max = 2, message = 'Masukan nomor umur anda dengan benar') ])
    
    alamat = StringField('Wilayah kota / Kabupaten', validators=[DataRequired(message = 'Masukan wilayah kota/kabupaten anda disini')])
    email = StringField('email', validators = [DataRequired(message = 'Masukan email anda disini'), Email(message = 'Masukan email anda dengan benar')])
    password = PasswordField('Password', validators = [DataRequired(message = 'Masukan password anda disini')])
    confirmpassword = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password', message = 'Masukan kembali password dengan benar')])

    submit = SubmitField ('Daftar Sekarang')

    def validate_ktp(self,ktp):
        user = User.query.filter_by(ktp = ktp.data).first()
        if user:
            raise ValidationError('Nomor ktp yang anda masukan telah terdaftar!')

    def validate_email(self,email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('Email yang anda masukan telah terdaftar!')


    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

class LoginForm (FlaskForm):
    email = StringField('Email', validators = [DataRequired(message = 'Masukan email anda disini'), Email(message = 'Masukan email anda dengan benar')])
    password = PasswordField('Password', validators = [DataRequired(message = 'Masukan password anda disini')])
    remember = BooleanField('Remember me')
    submit = SubmitField ('Masuk')

class ContactHistoryForm (FlaskForm):
    submit_test = SubmitField ('Lihat hasil')

class GejalaForm (FlaskForm):
    submit_gejala = SubmitField ('Lihat hasil')

class KondisiPenyertaForm (FlaskForm):
    submitaja = SubmitField ('Lihat hasil')

class TravelForm (FlaskForm):
    submitaja = SubmitField ('Lihat hasil')

