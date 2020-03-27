from .database import db
from .app import app
from flask import Flask, render_template, request, redirect, session, url_for
# url_for generates url (if you want to use css or codes which you made on your own)
from .models import User, Login, RoomAl1
import os

app.config["IMAGE_UPLOADS"] = 'static/img'
@app.route('/', methods=['POST','GET'])
def index():
    # if request.method == 'POST':
    #     # filter_by() <--- uses to filter the records in the table before the first() method will
    #     #                   execute/run
    #     # filter_by() <--- means if will look for the username and password entered by the user in
    #     #                   the form. both values should be on the same row/record
    #     # first() <--- this method will display/return the first occurence of the entered vaules
    #     login = Login.query.filter_by(uname=request.form['username'],password=request.form['password']).first()

    #     # example: uname = test, password = a <--- query will return FALSE since both data DO NOT BELONG
    #     #                                           to the same record
    #     # uname = test, password = test <--- query will return TRUE since both BELONGS TO THE SAME RECORD
    #     if login:
    #         return redirect('/viewall')
    #     else:
    #         return 'Error in logging in'
    #     print('success')
    # else:
    login_id = session['id']
    user = User.query.get_or_404(login_id)
    Al1user = RoomAl1.query.order_by(RoomAl1.uname).all()
    count = 0
    for i in Al1user:
        Al1user[count] = i.uname
        count += 1
    Al1user = list(set(Al1user))
    print(Al1user)


    return render_template('index.html',user=user,Al1user=Al1user)

@app.route('/signup',methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        signup = Login(email=request.form['mail'],password=request.form['pass'])
        # login = Login.query.filter_by(email=request.form['lemail'],password=request.form['lpass']).first()
        
        try:
            db.session.add(signup)
            db.session.commit()

            db.session.refresh(signup)
            print(signup.id)

            user  = User(login_id=signup.id, fname=request.form['fname'], lname=request.form['lname'],username=request.form['username'])
            db.session.add(user)
            db.session.commit()
            
            

            return redirect('/')
        except:
            return 'Error'
        
        # if login:
        #     return redirect('/viewall')
        # else:
        #     return 'Error in logging in'
        # print('success')

        # login = Login.query.filter_by(email=request.form['lemail'],password=request.form['lpass']).first()
        # session['id'] = login.id
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
        login = Login.query.filter_by(email=request.form['lemail'],password=request.form['lpass']).first()
        session['id'] = login.id
                # example: uname = test, password = a <--- query will return FALSE since both data DO NOT BELONG
        #                                           to the same record
        # uname = test, password = test <--- query will return TRUE since both BELONGS TO THE SAME RECORD
        if login:
            return redirect('/')
        else:
            return 'Error in logging in'
        print('success')
    else:
        return render_template('login.html')


@app.route('/roomAlgebra', methods=['POST','GET'])
def roomAlgebra():
    login_id = session['id']
    user = User.query.get_or_404(login_id)
    roomAl1 = RoomAl1.query.all()
    # roomAl1 = Login.query(login).join(roomAl1).filter(login.id==roomAl1.login_id)
    print("ルーム一覧",roomAl1)
    
    if request.method == 'POST':
        if 'photo' not in request.files:
            
            roomAl1 = RoomAl1(sentence=request.form['sentence'], uname=request.form['uname'],login_id=request.form['user_id'],pic=0)
            # try:
            db.session.add(roomAl1)
            db.session.commit()
            user_id= request.form['user_id']
            # uname = Login.query(login).join(roomAl1).filter(login.id==roomAl1.login_id)
            # uname = db.session.query(Login).join(roomAl1).filter(login.id==roomAl1.login_id)
            print("formユーザーid",user_id)
            print("はいってる")
            return redirect('/roomAlgebra')
        else:
            images = request.files['image']
            pic_name = images.filename
            print(pic_name)
            images.save(os.path.join(app.config["IMAGE_UPLOADS"], images.filename))
            roomAl1 = RoomAl1(sentence=request.form['sentence'], uname=request.form['uname'],login_id=request.form['user_id'],pic=pic_name)
            # try:
            db.session.add(roomAl1)
            db.session.commit()
            user_id= request.form['user_id']
            # uname = Login.query(login).join(roomAl1).filter(login.id==roomAl1.login_id)
            # uname = db.session.query(Login).join(roomAl1).filter(login.id==roomAl1.login_id)
            print("formユーザーid",user_id)
            print("はいってない")
            return redirect('/roomAlgebra')

            # except:
            #     print("formユーザーid",user_id)
            #     print("roomユーザーid",roomAl1.login_id)
            #     return 'Submit Error in room'
            
    else:
        return render_template('roomAlgebra.html', user=user,roomAl1=roomAl1)
    # return render_template('roomAlgebra.html')
# @app.route('/roomAlgebra', methods=['POST','GET'])
# def roomAlgebra():
#     roomAl1 = RoomAl1.query.all()
#     user = User.query.all()
    
#     return render_template('roomAlgebra.html', user=user,roomAl1=roomAl1)





@app.route('/viewall')
def viewAll(): 
    user = User.query.order_by(User.fname).all()

    return render_template('viewall.html', users=user)
    # return render_template('viewall.html')

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