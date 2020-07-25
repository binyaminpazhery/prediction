from flask import *
from database import *
public=Blueprint('public',__name__)

@public.route('/about',methods=['get','post'])
def about():
	return render_template('about.html')
	
@public.route('/',methods=['get','post'])
def homepage():
	return render_template('index.html')
@public.route('/login',methods=['get','post'])
def login():
	if 'submit' in request.form:
		username=request.form['username']
		password=request.form['password']
		q="select * from login where username='%s' and password='%s'"%(username,password)
		res=select(q)
		print(res)
		if res:
			session['loginid']=res[0]['log_id']
			print(res[0]['type'])
			if res[0]['type']=="staff":
				return redirect(url_for('employee.emphome'))
			if res[0]['type']=="admin":
				return redirect(url_for('admin.adminhome'))
			if res[0]['type']=="company":
				return redirect(url_for('company.comphome'))
		else:
			print('Invalid Username or Password')
	return render_template('login.html')

@public.route('/compregister',methods=['get','post'])
def compregister():
	data={}
	if 'submit' in request.form:
		companyname=request.form['companyname']
		address=request.form['address']
		phoneno=request.form['phoneno']
		emailid=request.form['emailid']
		username=request.form['username']
		password=request.form['password']
		q="insert into login values(null,'%s','%s','company')"%(username,password)
		id=insert(q)
		q="insert into company values(null,'%s','%s','%s','%s','%s')"%(id,companyname,address,phoneno,emailid)
		insert(q)
	return render_template('compregister.html')