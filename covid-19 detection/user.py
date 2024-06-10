from flask import *
from database import *
import uuid
from newcnn import *
user=Blueprint('user',__name__)

@user.route('/user_home',methods=['get','post'])
def user_home():
	if not session.get("lid") is None:
		data={}
		return render_template("user_home.html",data=data)
	else:
		return redirect(url_for('public.login'))




@user.route('/user_View_alzimer_details_and_symptoms',methods=['get','post'])
def user_View_alzimer_details_and_symptoms():
	if not session.get("lid") is None:
		data={}
		q="SELECT * FROM `alzimers` ORDER BY `alzimers_id` DESC"
		data['alz']=select(q)
		if 'action' in request.args:
			action=request.args['action']
			id=request.args['id']
		else:
			action=None
		if action=='sym':
			q="SELECT * FROM `symptoms` WHERE `alzimers_id`='%s' ORDER BY `symptom_id` DESC"%(id)
			data['sym']=res=select(q)
			if not res:
				flash('!! NO DATA FOUND !!')
		return render_template("user_View_alzimer_details_and_symptoms.html",data=data)
	else:
		return redirect(url_for('public.login'))

@user.route('/user_view_appointment',methods=['get','post'])
def user_view_appointment():
	data={}
	q="SELECT * FROM `appointment` INNER JOIN `doctor` USING(`doctor_id`) WHERE `user_id`='%s'"%(session['id'])
	data['view']=select(q)
	
	return render_template('user_view_appointment.html',data=data)






@user.route('/user_View_predicted_output',methods=['get','post'])
def user_View_predicted_output():
	if not session.get("lid") is None:
		data={}
		if 'submit' in request.form:
			data=request.files['data']
			path="static/uploads/"+str(uuid.uuid4())+data.filename
			print(path)
			data.save(path)
			res=predictcnn(path)
			print(res)
			val=""
			if res==0:
				val="Covid-19"
			if res==1:
				val="Normal"
			if res==2:
				val="Pneumonia"
			# if res==4:
			# 	val="normal"
			# if res==5:
			# 	val="Primary Endo with Secondary Perio"
			
			q="INSERT INTO `prediction` (`user_id`,`datasuploaded`,`output`) VALUES ('%s','%s','%s')"%(session['id'],path,val)
			insert(q)
			flash('UPLOADED')
			return redirect(url_for('user.user_View_predicted_output'))
		q="SELECT *,CONCAT(`firstname`,' ',`lastname`) AS `user` FROM `prediction` INNER JOIN `users` USING (`user_id`) WHERE user_id='%s' ORDER BY `prediction_id` DESC"%(session['id'])
		data['pre']=select(q)
		return render_template("user_View_predicted_output.html",data=data)
	else:
		return redirect(url_for('public.login'))






@user.route('/user_Upload_rating_for_the_output',methods=['get','post'])
def user_Upload_rating_for_the_output():
	if not session.get("lid") is None:
		data={}
		q="SELECT *,CONCAT(`firstname`,' ',`lastname`) AS `user` FROM `rating` INNER JOIN `users` USING (`user_id`) WHERE user_id='%s' ORDER BY `rating_id` DESC"%(session['id'])
		data['rate']=res=select(q)
		if 'submit' in request.form:
			rate=request.form['rate']
			feed=request.form['feed']
			if res:
				q="UPDATE `rating` SET `rated`='%s' , feedback='%s', `date`=CURDATE() WHERE `user_id`='%s'"%(rate,feed,session['id'])
				update(q)
				flash('RATED')
				return redirect(url_for('user.user_Upload_rating_for_the_output'))
			else:
				q="INSERT INTO `rating` (`user_id`,`rated`,`feedback`,`date`) VALUES ('%s','%s','%s',CURDATE())"%(session['id'],rate,feed)
				insert(q)
				flash('RATED')
				return redirect(url_for('user.user_Upload_rating_for_the_output'))
		return render_template("user_Upload_rating_for_the_output.html",data=data)
	else:
		return redirect(url_for('public.login'))

@user.route('/user_make_appointment',methods=['get','post'])
def user_make_appointment():
	data={}
	doctor_id=request.args['doctor_id']
	if 'submit' in request.form:
		appoinment=request.form['appoinment']
		q="SELECT * FROM `appointment` WHERE `doctor_id`='%s' "%(doctor_id)
		res=select(q)
		if res:
			flash("appoinment request already sent")
		else:
			q="INSERT INTO `appointment` VALUES(NULL,'%s','%s','%s','Appointment Fixed','500')"%(session['id'],doctor_id,appoinment)
			insert(q)

	q="SELECT * FROM `appointment` WHERE `user_id`='%s' and doctor_id='%s' "%(session['id'],doctor_id)
	data['view']=select(q)
	return render_template('user_make_appointment.html',data=data)



@user.route('/user_send_enquiry',methods=['get','post'])
def user_send_enquiry():
	data={}
	q="select * from doctor"
	data['res']=select(q)
	p="select *from enquiry where user_id='%s'"%(session['id'])
	eres=select(p)
	data['enquiry']=eres

	if 'submit' in request.form:
		enquiry=request.form['enquiry']	
		did=request.form['did']
		q="insert into enquiry values(null,'%s','%s','%s',curdate(),'pending')"%(session['id'],did,enquiry)
		insert(q)

		return redirect(url_for('user.user_send_enquiry'))

	if 'action' in request.args:
		action=request.args['action']
		cid=request.args['id']
	else:
		action=None

	if action=="delete":
		q="delete from enquiry where equiry_id='%s'"%(cid)
		delete(q)

		
		return redirect(url_for('user.user_send_enquiry'))
	return render_template('user_send_enquiry.html',data=data)

@user.route('/user_view_doctors',methods=['get','post'])
def user_view_doctors():
	data={}
	prediction_id=request.args['prediction_id']
	q="SELECT * FROM `doctor` "
	data['view']=select(q)
	

	return render_template('user_view_doctors.html',data=data,prediction_id=prediction_id)





# @user.route('/user_home',methods=['get','post'])
# def user_home():
# 	if not session.get("lid") is None:
# 		data={}
# 		return render_template("user_home.html",data=data)
# 	else:
# 		return redirect(url_for('public.login'))






# @user.route('/user_home',methods=['get','post'])
# def user_home():
# 	if not session.get("lid") is None:
# 		data={}
# 		return render_template("user_home.html",data=data)
# 	else:
# 		return redirect(url_for('public.login'))






# @user.route('/user_home',methods=['get','post'])
# def user_home():
# 	if not session.get("lid") is None:
# 		data={}
# 		return render_template("user_home.html",data=data)
# 	else:
# 		return redirect(url_for('public.login'))






# @user.route('/user_home',methods=['get','post'])
# def user_home():
# 	if not session.get("lid") is None:
# 		data={}
# 		return render_template("user_home.html",data=data)
# 	else:
# 		return redirect(url_for('public.login'))






# @user.route('/user_home',methods=['get','post'])
# def user_home():
# 	if not session.get("lid") is None:
# 		data={}
# 		return render_template("user_home.html",data=data)
# 	else:
# 		return redirect(url_for('public.login'))



@user.route('user_make_payment',methods=['get','post'])
def user_make_payment():
	data={}
	total=request.args['total']
	appointment_id=request.args['appointment_id']

	if 'btn' in request.form:
		name=request.form['name']
		number=request.form['number']
		exry=request.form['exry']
		q="INSERT INTO `payment` VALUES(NULL,'%s','%s',CURDATE())"%(appointment_id,total)
		insert(q)
		q="update appointment set appoin_status='paid' where appointment_id='%s'"%(appointment_id)
		update(q)

		flash(" Payment Successfull")
		return redirect(url_for('user.user_home',total=total,appointment_id=appointment_id))
	return render_template('user_make_payment.html',data=data,total=total,appointment_id=appointment_id)
@user.route('/user_view_remadys',methods=['get','post'])
def user_view_remadys():
	data={}
	q="SELECT * FROM `remady` WHERE `user_id`='%s'"%(session['id'])
	data['view']=select(q)
	
	return render_template('user_view_remadys.html',data=data)





