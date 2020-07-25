from flask import *
from database import *
import core
admin=Blueprint('admin',__name__)
@admin.route('/adminhome',methods=['get','post'])
def adminhome():
	return render_template('adminhome.html')

@admin.route('/adminstaff',methods=['get','post'])
def adminstaff():
	data={}
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="delete":
		q="delete  from staff where staff_id='%s'"%(id)
		delete(q)
	if action=="update":
		q="select * from staff where staff_id='%s'"%(id)
		res=select(q)
		data['updatestaff']=res
	if 'update' in request.form:
		firstname=request.form['firstname']
		lastname=request.form['lastname']
		dob=request.form['dob']
		designation=request.form['designation']
		place=request.form['place']
		qualification=request.form['qualification']
		phoneno=request.form['phoneno']
		emailid=request.form['emailid']
		username=request.form['username']
		password=request.form['password']
		q="update student set firstname='%s',lastname='%s',dob='%s',designation='%s',place='%s',qualification='%s',phoneno='%s',emailid='%s',username='%s',password='%s'where staff_id='%s'"%(firstname,lastname,dob,designation,place,qualification,phoneno,emailid,username,password,id)
		update(q)
		return redirect(url_for('admin.adminstaff'))
	if 'submit' in request.form:
		firstname=request.form['firstname']
		lastname=request.form['lastname']
		dob=request.form['dob']
		designation=request.form['designation']
		place=request.form['place']
		qualification=request.form['qualification']
		phoneno=request.form['phoneno']
		emailid=request.form['emailid']
		username=request.form['username']
		password=request.form['password']
		q="insert into login values(null,'%s','%s','staff')"%(username,password)
		id=insert(q)
		q="insert into staff values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(id,firstname,lastname,dob,designation,place,qualification,phoneno,emailid)
		insert(q)
	q="select * from staff"
	res=select(q)
	data['staff']=res
	return render_template('adminstaff.html',data=data)

@admin.route('/adminstudent',methods=['get','post'])
def adminstudent():
	data={}
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="delete":
		q="delete  from student where student_id='%s'"%(id)
		delete(q)
	if action=="update":
		q="select * from student where student_id='%s'"%(id)
		res=select(q)
		data['updatestd']=res
	if 'update' in request.form:
		firstname=request.form['firstname']
		lastname=request.form['lastname']
		dob=request.form['dob']
		gender=request.form['gender']
		phoneno=request.form['phoneno']
		emailid=request.form['emailid']
		housename=request.form['housename']
		place=request.form['place']
		pincode=request.form['pincode']
		guardianname=request.form['guardianname']
		relationship=request.form['relationship']
		guardianphone=request.form['guardianphone']
		courseid=request.form['course_id']
		interest=request.form['interest']
		q="update student set firstname='%s',lastname='%s',dob='%s',gender='%s',phoneno='%s',emailid='%s',housename='%s',place='%s',pincode='%s',guardianname='%s',relationship='%s',guardianphone='%s',course_id='%s',interest='%s' where student_id='%s'"%(firstname,lastname,dob,gender,phoneno,emailid,housename,place,pincode,guardianname,relationship,guardianphone,courseid,interest,id)
		update(q)
		return redirect(url_for('admin.adminstudent'))
	if 'submit' in request.form:
		firstname=request.form['firstname']
		lastname=request.form['lastname']
		dateofbirth=request.form['dob']
		gender=request.form['gender']
		phoneno=request.form['phoneno']
		emailid=request.form['emailid']
		housename=request.form['housename']
		place=request.form['place']
		pincode=request.form['pincode']
		guardianname=request.form['guardianname']
		relationship=request.form['relationship']
		guardianphone=request.form['guardianphone']
		courseid=request.form['course_id']
		interest=request.form['interest']
		q="insert into student values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(firstname,lastname,dateofbirth,gender,phoneno,emailid,housename,place,pincode,guardianname,relationship,guardianphone,courseid,interest)
		insert(q)
	q="select * from course"
	res=select(q)
	data['course']=res
	q="select * from student inner join course using(course_id)"
	res=select(q)
	data['student']=res
	return render_template('adminstudent.html',data=data)

@admin.route('/adminviewcompany',methods=['get','post'])
def adminviewcompany():
	data={}
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="delete":
		q="delete  from company where company_id='%s'"%(id)
		delete(q)
	if action=="update":
		q="select * from company where company_id='%s'"%(id)
		res=select(q)
		data['updatecomp']=res
	if 'update' in request.form:
		companyname=request.form['companyname']
		address=request.form['address']
		phoneno=request.form['phoneno']
		emailid=request.form['emailid']
		username=request.form['username']
		password=request.form['password']
		q="update company set companyname='%s',address='%s',phoneno='%s',emailid='%s',username='%s',password='%s' where company_id='%s'"%(companyname,address,phoneno,emailid,username,password,id)
		update(q)
		return redirect(url_for('admin.adminviewcompany'))
	if 'submit' in request.form:
		companyname=request.form['companyname']
		address=request.form['address']
		phoneno=request.form['phoneno']
		emailid=request.form['emailid']
		username=request.form['username']
		password=request.form['password']
		q="insert into login values(null,'%s','%s','company')"%(username,password)
		id=insert(q)
		q="insert into company values(null,'%s','%s','%s','%s','%s','%s')"%(id,companyname,address,phoneno,emailid)
		insert(q)
	q="select * from company"
	res=select(q)
	data['company']=res
	return render_template('adminviewcompany.html',data=data)

@admin.route('/admincourse',methods=['get','post'])
def admincourse():
	data={}
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="delete":
		q="delete  from course where course_id='%s'"%(id)
		delete(q)
	if action=="update":
		q="select * from course where course_id='%s'"%(id)
		res=select(q)
		data['updatecourse']=res
	if 'update' in request.form:
		coursename=request.form['coursename']
		description=request.form['description']
		q="update course set coursename='%s',description='%s' where course_id='%s'"%(coursename,description,id)
		update(q)
		return redirect(url_for('admin.admincourse'))
	if 'submit' in request.form:
		coursename=request.form['coursename']
		description=request.form['description']
		q="insert into course values(null,'%s','%s')"%(coursename,description)
		insert(q)
	q="select * from course"
	res=select(q)
	data['course']=res
	return render_template('admincourse.html',data=data)




@admin.route('/admincriteria',methods=['get','post'])
def admincriteria():
	data={}
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="delete":
		q="delete  from tbl_criteria where criteria_id='%s'"%(id)
		delete(q)
	# if action=="update":
	# 	q="select * from course where course_id='%s'"%(id)
	# 	res=select(q)
	# 	data['updatecourse']=res
	# if 'update' in request.form:
	# 	coursename=request.form['coursename']
	# 	description=request.form['description']
	# 	q="update course set coursename='%s',description='%s' where course_id='%s'"%(coursename,description,id)
	# 	update(q)
	# 	return redirect(url_for('admin.admincriteria'))
	if "add_criteria" in request.form:
		criteria_name = request.form['criteria_name']
		criteria_level_range = request.form['criteria_level_range']
		criteria_type = request.form['criteria_type']
		q = "INSERT INTO tbl_criteria(criteria_name, criteria_level_range, criteria_type) values('%s','%s','%s')" % (criteria_name,criteria_level_range,criteria_type)
		insert(q)
		# flash("Added successfully")
		return redirect(url_for('admin.admincriteria'))
    
	q="select * from tbl_criteria"
	res=select(q)
	data['criteria']=res
	return render_template('admincriteria.html',data=data)



@admin.route('/train')
def train():
    score = core.train()
    print(score)
    return render_template('model_train.html',score = score)




@admin.route('/adminviewpredict',methods=['get','post'])
def adminviewpredict():
	q = "select * from selection inner join student using(student_id) inner join course using(course_id)"
	res = select(q)
	return render_template('adminviewpredict.html',data=res)

