from flask import render_template, url_for, flash, redirect, request
from flaskblog.__innit__ import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, TestForm
from flaskblog.models import User, Result
from flask_login import login_user, logout_user, current_user, login_required


@app.route('/')
@app.route('/home')
def home():
    return render_template('newhome.html', title = 'Home')

@app.route('/main')
def main():
    return render_template('main.html')



@app.route('/testme', methods = ['GET','POST'])
def testme():
    form = TestForm()
    if form.validate_on_submit():
        result = Result(riwayat_jalan = form.riwayat_jalan.data, riwayat_kontak = form.riwayat_kontak.data, riwayat_kontak_pdp = form.riwayat_kontak_pdp.data, gejala_batuk = form.gejala_batuk.data, testresultuser = current_user)
        db.session.add(result)
        db.session.commit()
        flash(f'Input telah berhasil !', 'success')
        return redirect(url_for('profile'))
    return render_template('testme2.html', title = 'Cek resiko infeksi online', form = form)

@app.route('/register', methods = ['GET','POST'])
def register():
   form = RegistrationForm()
   if form.validate_on_submit(): 
       hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
       user = User(ktp = form.ktp.data, nama = form.nama.data, jenis_kelamin = form.jenis_kelamin.data, alamat = form.alamat.data, email = form.email.data, password = hashed_password)
       db.session.add(user)
       db.session.commit()
       flash(f'Akun berhasil terdaftar untuk {form.nama.data}', 'success')
       return redirect(url_for('login'))
   return render_template('pendaftaran.html', title = 'Halaman Pendaftaran', form = form)

@app.route('/profile')
@login_required
def profile():
   posts = Result.query.all()
   return render_template('profile.html', title = ' Profil', posts=posts)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('testme'))
        else:
            flash(f'Masuk gagal, mohon cek kembali email dan password anda!','danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))