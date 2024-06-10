from flask import *
from database import *
import uuid 
from newcnn import *

api=Blueprint('api',__name__)


@api.route("/login")
def login():
    data={}
    uname=request.args['username']
    password=request.args['password']
    q="select * from login where username='%s' and password='%s'"%(uname,password)
    res=select(q)
    if res:
        data['status']="success"
        data['data']=res
    else:
        data['status']="failed"
    return str(data)


@api.route("/reg",methods=['get','post'])
def reg():
    data={}

    fname=request.args['fname']
    lname=request.args['lname']
    place=request.args['place']
    phone=request.args['phone']
    email=request.args['email']
    username=request.args['uname']
    password=request.args['pass']

    q="select * from login where username='%s'"%(username)
    rep=select(q)

    if rep:
        data['status']='already'
    else:
        q="insert into `login` values(NULL,'%s','%s','user') "%(username,password)
        ref=insert(q)
        v="insert into `users` values(NULL,'%s','%s','%s','%s','%s','%s') "%(ref,fname,lname,place,phone,email)
        insert(v)
        data['status']='success'
    data['method']="reg"
    return str(data)



@api.route("/view_remady")
def view_remady():
    data={}
    q="SELECT * FROM remady"
    res=select(q)
    if res:
        data['status']="success"
        data['data']=res
    else:
        data['status']="failed"
    data['method']="view_remady"
    return str(data)


@api.route("/view_doc")
def view_doc():
    data={}
    q="SELECT *,concat(fname,'',lname) as name FROM doctor"
    res=select(q)
    if res:
        data['status']="success"
        data['data']=res
    else:
        data['status']="failed"
    data['method']="view_doc"
    return str(data)


@api.route('/viewenquiry')
def viewenquiry():
    data={}
    lid=request.args['lid']
    z="select * from enquiry where user_id= (select user_id from users where login_id='%s')"%(lid)
    res=select(z)

    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    data['method']="viewenquiry"
    return str(data)


@api.route("/addenquiry")
def addenquiry():
    complaint=request.args['complaint']
    lid=request.args['lid']
    did=request.args['did']
    data={}

    q="insert into enquiry values (null,(select user_id from users where login_id='%s'),'%s','%s','pending',curdate())"%(lid,did,complaint)
    insert(q)
    data['status']="success"
    data['method']="addenquiry"
    return str(data)


@api.route('/view_appoinments')
def view_appoinments():
    data={}
    lid=request.args['lid']
    z="SELECT *,concat(fname,'',lname) as name FROM `appointment` INNER JOIN `doctor` USING(`doctor_id`) where user_id= (select user_id from users where login_id='%s')"%(lid)
    res=select(z)

    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    data['method']="view_appoinments"
    return str(data)



@api.route('/addrating')
def addrating():
    data={}
    lid=request.args['lid']
    rate=request.args['rating']
    feed = ""
    if float(rate)  < 2.5:
        feed="bad"
    elif float(rate) < 3.5:
        feed="good"
    elif float(rate) > 3.5:
        feed="Perfect"

    q="SELECT *,CONCAT(`firstname`,' ',`lastname`) AS `user` FROM `rating` INNER JOIN `users` USING (`user_id`) WHERE user_id=(select user_id from users where login_id='%s') ORDER BY `rating_id` DESC"%(lid)
    data['rate']=res=select(q)

    if res:
        q="UPDATE `rating` SET `rated`='%s' , feedback='%s', `date`=CURDATE() WHERE `user_id`=(select user_id from users where login_id='%s')"%(rate,feed,lid)
        update(q)
    else:
        q="INSERT INTO `rating` (`user_id`,`rated`,`feedback`,`date`) VALUES ((select user_id from users where login_id='%s'),'%s','%s',CURDATE())"%(lid,rate,feed)
        insert(q)

    data['status']="success"
    data['method']="addrating"
    return str(data)


@api.route('/viewrating')
def viewrating():
    data={}
    lid=request.args['lid']
    rating=""
    z="select * from rating where user_id=(select user_id from users where login_id='%s')"%(lid)
    res=select(z)
    if res:
        rating=res[0]['rated']

    if res:
        data['status']='okey'
        data['data']=rating
    else:
        data['status']='failed'
    data['method']='viewrating'
    return str(data)

@api.route('/view_out')
def view_out():
    data={}
    lid=request.args['lid']
    rating=""
    z="select * from prediction where user_id=(select user_id from users where login_id='%s')"%(lid)
    res=select(z)

    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    data['method']='view_out'
    return str(data)




@api.route('/user_prediction',methods=['get','post'])
def user_prediction():
    data={}
    lid=request.form['lid']
    data=request.files['image']
    path="static/uploads/"+str(uuid.uuid4())+data.filename
    print(path)
    data.save(path)
    res=predictcnn(path)
    print(res)
    val=""
    if res==0:
        val="Primary Endodontic  Lesion"
    if res==1:
        val="Primary Perio with Secondary Endo"
    if res==2:
        val="Primary Periodontal Lesion"
    if res==3:
        val="True Combined Lesions"
    if res==4:
        val="normal"
    if res==5:
        val="Primary Endo with Secondary Perio"
    
    q="INSERT INTO `prediction` VALUES (null,(select user_id from users where login_id='%s'),'%s','%s')"%(lid,path,val)
    insert(q)
    flash('UPLOADED')
    return str(data)
