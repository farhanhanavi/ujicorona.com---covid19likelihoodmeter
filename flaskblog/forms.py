from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DecimalField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User



class RegistrationForm (FlaskForm):
    nama = StringField('Nama', validators = [DataRequired(message = 'Masukan nama anda disini')])
    ktp = StringField('Nomor KTP', validators = [DataRequired(message = 'Masukan ktp anda disini'), Length(min = 16, max = 16, message = 'Masukan nomor ktp anda dengan benar') ])
    nomor_hp = StringField('Nomor Handphone', validators = [DataRequired(message = 'Masukan nomor handphone anda disini')])
    umur = StringField('Umur', validators = [DataRequired(message = 'Masukan umur anda disini'), Length(min = 0, max = 2, message = 'Masukan nomor umur anda dengan benar') ])
    jenis_kelamin = StringField('Jenis Kelamin (P/W)', validators=[DataRequired(message = 'Masukan jenis kelamin anda disini'), Length(min = 1, max = 1, message = 'Masukan P untuk pria dan W untuk wanita')])
    alamat = StringField('Alamat tempat tinggal', validators=[DataRequired(message = 'Masukan alamat anda disini')])
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
    email = StringField('email', validators = [DataRequired(message = 'Masukan email anda disini'), Email(message = 'Masukan email anda dengan benar')])
    password = PasswordField('Password', validators = [DataRequired(message = 'Masukan password anda disini')])
    remember = BooleanField('Remember me')
    submit = SubmitField ('Masuk')

class ContactHistoryForm (FlaskForm):
    riwayat_jalan = StringField('Dalam 14-30 hari terakhir, apakah anda bepergian ke kota/negara terjangkit COVID19 (Y/N)?', validators = [DataRequired(message = 'Mohon jawab pertanyaan ini')])
    riwayat_kontak = StringField('Dalam 14-30 hari terakhir, apakah anda melakukan kontak dengan Pasien Probabel/Konfirmasi (Y/N) ?', validators = [DataRequired(message = 'Mohon jawab pertanyaan ini')])
    riwayat_kontak_pdp = StringField('Dalam 14-30 hari terakhir, apakah anda melakukan kontak dengan Pasien Dalam Pengawasan (Y/N)?', validators = [DataRequired(message = 'Mohon jawab pertanyaan ini')])
    submit_test = SubmitField ('Lihat hasil')


class GejalaForm (FlaskForm):
    demam = StringField('Apakah anda mengalami demam (Y/N)?', validators = [DataRequired(message = 'Mohon jawab pertanyaan ini')])
    batuk = StringField('Apakah anda mengalami batuk (Y/N) ?', validators = [DataRequired(message = 'Mohon jawab pertanyaan ini')])
    pilek = StringField('Apakah anda mengalami pilek (Y/N)', validators = [DataRequired(message = 'Mohon jawab pertanyaan ini')])
    nyeri_tenggorokan = StringField('Apakah mengalami nyeri tenggorokan (Y/N)?', validators = [DataRequired(message = 'Mohon jawab pertanyaan ini')])
    sesak = StringField('Apakah mengalami sesak nafas (Y/N)?', validators = [DataRequired(message = 'Mohon jawab pertanyaan ini')])
    submit_gejala = SubmitField ('Lihat hasil')

