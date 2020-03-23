from .database import db
from .app import app
from flask import Flask, render_template, request, redirect
# url_for generates url (if you want to use css or codes which you made on your own)
from .models import User, Login

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        # filter_by() <--- uses to filter the records in the table before the first() method will
        #                   execute/run
        # filter_by() <--- means if will look for the username and password entered by the user in
        #                   the form. both values should be on the same row/record
        # first() <--- this method will display/return the first occurence of the entered vaules
        login = Login.query.filter_by(uname=request.form['username'],password=request.form['password']).first()

        # example: uname = test, password = a <--- query will return FALSE since both data DO NOT BELONG
        #                                           to the same record
        # uname = test, password = test <--- query will return TRUE since both BELONGS TO THE SAME RECORD
        if login:
            return redirect('/viewall')
        else:
            return 'Error in logging in'
        print('success')
    else:
        return render_template('login.html')

@app.route('/signup',methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        login = Login(uname=request.form['username'], password=request.form['pass'])
        # signup = Login.query.filter_by(uname=request.form['name2'],password=request.form['pass2']).first()
        
        try:
            db.session.add(login)
            db.session.commit()

            db.session.refresh(login)
            print(login.id)

            user  = User(login_id=login.id, name=request.form['name'], address=request.form['address'], number=request.form['number'])
            db.session.add(user)
            db.session.commit()

            return redirect('/viewall')
        except:
            return 'Error'
        
        # if signup:
        #     return redirect('/viewall')
        # else:
        #     return 'Error in logging in'
        # print('success')
    else:
        return render_template('signup.html')


@app.route('/login',methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        # filter_by() <--- uses to filter the records in the table before the first() method will
        #                   execute/run
        # filter_by() <--- means if will look for the username and password entered by the user in
        #                   the form. both values should be on the same row/record
        # first() <--- this method will display/return the first occurence of the entered vaules
        login = Login.query.filter_by(uname=request.form['username'],password=request.form['password']).first()

        # example: uname = test, password = a <--- query will return FALSE since both data DO NOT BELONG
        #                                           to the same record
        # uname = test, password = test <--- query will return TRUE since both BELONGS TO THE SAME RECORD
        if login:
            return redirect('/viewall')
        else:
            return 'Error in logging in'
        print('success')
    else:
        return render_template('login.html')



@app.route('/viewall')
def viewAll(): 
    user = User.query.order_by(User.name).all()

    return render_template('viewall.html', users=user)

@app.route('/delete/<int:id>')
def delete(id):
    user_to_delete = User.query.get_or_404(id)

    try:
        db.session.delete(user_to_delete)
        db.session.commit()

        return redirect('/viewall')
    except:
        return 'Error in deleting user'

@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    # 404 <--- NOT FOUNT or NOT EXISTING
    user=User.query.get_or_404(id)

    if request.method == 'POST':
        # request.form['name'] <---- this will get the value entered by the user in the NAME failed
        #                               from the form
        user.name= request.form['name']
        user.address = request.form['address']
        user.number = request.form['number']
        print(user.name)
        try:
            # commit() <--- equivalent to GO/SAVE//EXECUTE
            db.session.commit()
            return redirect('/viewall')
        except:
            return 'Error in updating'
    else:
        return render_template('update.html', user=user)