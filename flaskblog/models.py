from datetime import datetime
from flaskblog.__innit__ import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    ktp = db.Column(db.String(16), unique = True, nullable = False)
    nama = db.Column(db.String(30), nullable = False)
    nomor_hp = db.Column(db.String(15), nullable = False)
    umur = db.Column(db.String(2), nullable = False)
    jenis_kelamin = db.Column(db.String(1), nullable = False)
    alamat = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(100), nullable = False)

    image_file = db.Column(db.String(20), nullable = False, default='default.jpg')
    result = db.relationship('ContactHistory', backref = 'testresultuser', lazy = True)
    symptoms = db.relationship('Symptoms', backref = 'testgejalauser', lazy = True)
    def __repr__(self):
        return f"user('{self.ktp}', '{self.nama}', '{self.image_file}', '{self.email}', '{self.password}')"



class ContactHistory(db.Model):
    post_id = db.Column(db.Integer, primary_key = True)
    riwayat_jalan = db.Column(db.String(3), nullable = False)
    riwayat_kontak = db.Column(db.String(3), nullable = False)
    riwayat_kontak_pdp = db.Column(db.String(3), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    def __repr__(self):
        return f"result('{self.riwayat_jalan}', '{self.riwayat_kontak}', '{self.riwayat_kontak_pdp}', '{self.gejala_batuk}')"


class Symptoms(db.Model):
    symtomsid = db.Column(db.Integer, primary_key = True)
    demam = db.Column(db.String(3), nullable = False)
    batuk = db.Column(db.String(3), nullable = False)
    pilek = db.Column(db.String(3), nullable = False)
    nyeri_tenggorokan = db.Column(db.String(3), nullable = False)
    sesak = db.Column(db.String(3), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    def __repr__(self):
        return f"result('{self.riwayat_jalan}', '{self.riwayat_kontak}', '{self.riwayat_kontak_pdp}', '{self.gejala_batuk}')"