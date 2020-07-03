from flask import render_template, url_for, flash, redirect, request
from flaskblog.__innit__ import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, ContactHistoryForm, GejalaForm, KondisiPenyertaForm, TravelForm
from flaskblog.models import *
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
        

        if request.form['form_kontak_pdp'] == 'y':
            contact_history = ContactHistory(riwayat_jalan = request.form['form_jalan'], riwayat_kontak = request.form['form_kontak'], riwayat_kontak_pdp = request.form['form_kontak_pdp'], contactresult = '3', testcontactuser = current_user)
            db.session.add(contact_history)
            db.session.commit()
            flash(f'Input riwayat bepergian berhasil !', 'success')
            return redirect(url_for('riwayatgejala'))
        
        if request.form['form_kontak'] == 'y':
            contact_history = ContactHistory(riwayat_jalan = request.form['form_jalan'], riwayat_kontak = request.form['form_kontak'], riwayat_kontak_pdp = request.form['form_kontak_pdp'], contactresult = '2', testcontactuser = current_user)
            db.session.add(contact_history)
            db.session.commit()
            flash(f'Input riwayat bepergian berhasil !', 'success')
            return redirect(url_for('riwayatgejala'))

        if request.form['form_jalan'] == 'y':
            contact_history = ContactHistory(riwayat_jalan = request.form['form_jalan'], riwayat_kontak = request.form['form_kontak'], riwayat_kontak_pdp = request.form['form_kontak_pdp'], contactresult = '1', testcontactuser = current_user)
            db.session.add(contact_history)
            db.session.commit()
            flash(f'Input riwayat bepergian berhasil !', 'success')
            return redirect(url_for('riwayatgejala'))

        else: 
            contact_history = ContactHistory(riwayat_jalan = request.form['form_jalan'], riwayat_kontak = request.form['form_kontak'], riwayat_kontak_pdp = request.form['form_kontak_pdp'], contactresult = '0', testcontactuser = current_user)
            db.session.add(contact_history)
            db.session.commit()
            flash(f'Input riwayat bepergian berhasil !', 'success')
            return redirect(url_for('riwayatgejala'))
    return render_template('riwayatbepergian.html', title = 'Cek resiko infeksi online', form = form)


@app.route('/riwayatgejala', methods = ['GET','POST'])
def riwayatgejala():
    form = GejalaForm()
    if form.validate_on_submit():

        if request.form['demam'] == 'y' or request.form['batuk'] == 'y' or request.form['pilek'] == 'y' or request.form['nyeri_tenggorokan'] == 'y' or request.form['sesak_nafas'] == 'y':    
                symptoms = Symptoms(demam = request.form['demam'], batuk = request.form['batuk'], pilek = request.form['pilek'], nyeri_tenggorokan = request.form['nyeri_tenggorokan'], sesak = request.form['sesak_nafas'], symptomsresult = '1', testsymptomsuser = current_user)
                #tidur = request.form['tidur']#,  , menggigil = request.form['menggigil'], sakit_kepala = request.form['sakitkepala'], kelelahan = request.form['kelelahan'], nyeri_otot = request.form['nyeri_otot'], mual = request.form['mual'], nyeri_perut = request.form['nyeri_perut'], diare = request.form['diare'], symptomsresult = '1', testsymptomsuser = current_user)
                db.session.add(symptoms)
                db.session.commit()

                usersymptoms = Symptoms.query.filter_by(id = current_user.id).order_by(Symptoms.symptomsid.desc()).first()
                usercontact = ContactHistory.query.filter_by(id = current_user.id).order_by(ContactHistory.contact_id.desc()).first()    

                if usercontact.contactresult == 1 and usersymptoms.symptomsresult == 1:
                    userresult = Categories(id = current_user.id, contact_result = usercontact.contactresult,categories = 'ODP', symptoms_result= usersymptoms.symptomsresult)
                    db.session.add(userresult)
                    db.session.commit()
                    flash(f'Input telah berhasil !', 'success')
                    return redirect(url_for('profile'))
                if usercontact.contactresult == 2 and usersymptoms.symptomsresult == 1:
                    userresult = Categories(id = current_user.id, contact_result = usercontact.contactresult,categories = 'PDP', symptoms_result= usersymptoms.symptomsresult)
                    db.session.add(userresult)
                    db.session.commit()
                    flash(f'Input telah berhasil !', 'success')
                    return redirect(url_for('profile'))
                if usercontact.contactresult == 3 and usersymptoms.symptomsresult == 1:
                    userresult = Categories(id = current_user.id, contact_result = usercontact.contactresult,categories = 'Self Isolation', symptoms_result= usersymptoms.symptomsresult)
                    db.session.add(userresult)
                    db.session.commit()
                    flash(f'Input telah berhasil !', 'success')
                    return redirect(url_for('profile'))
                else:
                    userresult = Categories(id = current_user.id, contact_result = usercontact.contactresult,categories = '0', symptoms_result= usersymptoms.symptomsresult)
                    db.session.add(userresult)
                    db.session.commit()
                flash(f'Input telah berhasil !', 'success')
                return redirect(url_for('profile'))
        else:
                symptoms = Symptoms(demam = request.form['demam'], batuk = request.form['batuk'], pilek = request.form['pilek'], nyeri_tenggorokan = request.form['nyeri_tenggorokan'], sesak = request.form['sesak_nafas'], symptomsresult = '0', testsymptomsuser = current_user)
                #tidur = request.form['tidur']#,  , menggigil = request.form['menggigil'], sakit_kepala = request.form['sakitkepala'], kelelahan = request.form['kelelahan'], nyeri_otot = request.form['nyeri_otot'], mual = request.form['mual'], nyeri_perut = request.form['nyeri_perut'], diare = request.form['diare'], symptomsresult = '1', testsymptomsuser = current_user)
                db.session.add(symptoms)
                db.session.commit()
            
                usersymptoms = Symptoms.query.filter_by(id = current_user.id).order_by(Symptoms.symptomsid.desc()).first()
                usercontact = ContactHistory.query.filter_by(id = current_user.id).order_by(ContactHistory.contact_id.desc()).first()     
                
                if usercontact.contactresult == 1 and usersymptoms.symptomsresult == 0:
                    userresult = Categories(id = current_user.id, contact_result = usercontact.contactresult,categories = 'Self Isolation', symptoms_result= usersymptoms.symptomsresult)
                    db.session.add(userresult)
                    db.session.commit()
                    flash(f'Input telah berhasil !', 'success')
                    return redirect(url_for('profile'))
                if usercontact.contactresult == 2 and usersymptoms.symptomsresult == 0:
                    userresult = Categories(id = current_user.id, contact_result = usercontact.contactresult,categories = 'KERT', symptoms_result= usersymptoms.symptomsresult)
                    db.session.add(userresult)
                    db.session.commit()
                    flash(f'Input telah berhasil !', 'success')
                    return redirect(url_for('profile'))
                if usercontact.contactresult == 3 and usersymptoms.symptomsresult == 0:
                    userresult = Categories(id = current_user.id, contact_result = usercontact.contactresult,categories = 'KERR', symptoms_result= usersymptoms.symptomsresult)
                    db.session.add(userresult)
                    db.session.commit()
                    flash(f'Input telah berhasil !', 'success')
                    return redirect(url_for('profile'))  
                else:
                    userresult = Categories(id = current_user.id, contact_result = usercontact.contactresult,categories = 'sehat', symptoms_result= usersymptoms.symptomsresult)
                    db.session.add(userresult)
                    db.session.commit()
                    flash(f'Input telah berhasil !', 'success')
                    return redirect(url_for('profile'))  
    return render_template('riwayatgejala.html', title = 'Cek resiko infeksi online', form = form)


@app.route('/register', methods = ['GET','POST'])
def register():
   form = RegistrationForm()
   if form.validate_on_submit(): 
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(ktp = form.ktp.data, nama = form.nama.data, jenis_kelamin = request.form['jeniskelamin'], alamat = form.alamat.data, email = form.email.data, nomor_hp = form.nomor_hp.data, umur = form.umur.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Akun berhasil terdaftar untuk {form.nama.data}', 'success')
        return redirect(url_for('login'))
   return render_template('pendaftaran.html', title = 'Halaman Pendaftaran', form = form)


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



@app.route('/profile')
@login_required
def profile():
   post = Categories.query.filter_by(id = current_user.id)
   return render_template('profile.html', title = ' Profil', posts=post)

@app.route('/kondisipenyerta', methods=['GET', 'POST'] )
@login_required
def kondisi_penyerta():
   form = KondisiPenyertaForm()
  
   
   return render_template('kondisipenyerta.html', title = ' Profil', form=form)

@app.route('/travel')
@login_required
def travel():
   form = TravelForm()
   
   return render_template('travel.html', title = ' Profil', form=form)


