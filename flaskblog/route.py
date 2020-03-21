from flask import render_template, url_for, flash, redirect
from flaskblog.__innit__ import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user

posts = [

    {
        'author'    : 'Corey',
        'title'     : 'Blog post 1',
        'content'   : '1st content',
        'date'      : '19 April'
    },
    {
        'author'    : 'Shaffer',
        'title'     : 'Blog post 2',
        'content'   : '1st content',
        'date'      : '20 April'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = posts)

@app.route('/about')
def about():
    return render_template('about.html', title = 'about page')

@app.route('/testme', methods = ['GET','POST'])
def testme():
    return render_template('testme.html', title = 'Cek resiko infeksi online')

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

@app.route('/profile', methods = ['GET','POST'])
def profile():
   return render_template('profile.html', title = ' Profil', posts=posts)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('home'))
        else:
            flash(f'Masuk gagal, mohon cek kembali email dan password anda!','danger')
    return render_template('login.html', title='Login', form=form)