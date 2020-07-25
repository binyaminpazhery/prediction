from flask import *
from database import *

employee=Blueprint('employee',__name__)

@employee.route('/emphome',methods=['get','post'])
def emphome():
	return render_template('emphome.html')

@employee.route('/empviewstud',methods=['get','post'])
def empviewstud():
	data={}
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
	return render_template('empviewstud.html',data=data)


@employee.route('/student_criteria_manage/',methods=['get','post'])
def student_criteria_manage():
	q = "select * from tbl_criteria"
	res = select(q)
	if "add_stud_criteria" in request.form:
		stud_id = request.args['id']
		for row in res:
			name  = "criteria_" + str(row['criteria_id'])
			if name in request.form:
				level = request.form[name]
				criteria_id = row['criteria_id']
				q = "select * from tbl_stud_criteria where criteria_id='%s' and stud_id='%s'" % (criteria_id,stud_id)
				if(len(select(q)) == 0):
					q = "insert into tbl_stud_criteria(stud_id,criteria_id,criteria_level)values('%s','%s','%s')" %(stud_id,criteria_id,level)
					insert(q)
				else:
					q = "update tbl_stud_criteria set criteria_level='%s' where criteria_id='%s' and stud_id='%s' " % (level,criteria_id,stud_id)
					update(q)
		# flash("Inserted")
		return redirect(url_for('employee.student_criteria_manage'))
	
	return render_template('student_criteria_manage.html',data = res)