from flask import render_template, url_for, flash, redirect, request
from flaskblog.__innit__ import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, ContactHistoryForm, GejalaForm
from flaskblog.models import User, ContactHistory, Symptoms
from flask_login import login_user, logout_user, current_user, login_required


@app.route('/')
@app.route('/home')
def home():
    return render_template('newhome.html', title = 'Home')

@app.route('/main')
def main():
    return render_template('main.html')



@app.route('/riwayatbepergian', methods = ['GET','POST'])
def riwayatbepergian():
    form = ContactHistoryForm()
    if form.validate_on_submit():
        contact_history = ContactHistory(riwayat_jalan = form.riwayat_jalan.data, riwayat_kontak = form.riwayat_kontak.data, riwayat_kontak_pdp = form.riwayat_kontak_pdp.data, testresultuser = current_user)
        db.session.add(contact_history)
        db.session.commit()
        flash(f'Input riwayat bepergian berhasil !', 'success')
        return redirect(url_for('riwayatgejala'))
    return render_template('riwayatbepergian.html', title = 'Cek resiko infeksi online', form = form)


@app.route('/riwayatgejala', methods = ['GET','POST'])
def riwayatgejala():
    form = GejalaForm()
    if form.validate_on_submit():
        symptoms = Symptoms(demam = form.demam.data, batuk = form.batuk.data, pilek = form.pilek.data, nyeri_tenggorokan = form.nyeri_tenggorokan.data, sesak = form.sesak.data, testgejalauser = current_user)
        db.session.add(symptoms)
        db.session.commit()
        flash(f'Input telah berhasil !', 'success')
        return redirect(url_for('profile'))
    return render_template('riwayatgejala.html', title = 'Cek resiko infeksi online', form = form)


@app.route('/register', methods = ['GET','POST'])
def register():
   form = RegistrationForm()
   if form.validate_on_submit(): 
       hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
       user = User(ktp = form.ktp.data, nama = form.nama.data, jenis_kelamin = form.jenis_kelamin.data, alamat = form.alamat.data, email = form.email.data, nomor_hp = form.nomor_hp.data, umur = form.umur.data, password = hashed_password)
       db.session.add(user)
       db.session.commit()
       flash(f'Akun berhasil terdaftar untuk {form.nama.data}', 'success')
       return redirect(url_for('login'))
   return render_template('pendaftaran.html', title = 'Halaman Pendaftaran', form = form)

@app.route('/profile')
@login_required
def profile():
   post = ContactHistory.query.all()
   return render_template('profile.html', title = ' Profil', posts=post)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('riwayatbepergian'))
        else:
            flash(f'Masuk gagal, mohon cek kembali email dan password anda!','danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))