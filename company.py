from flask import *
from database import *
import core

company=Blueprint('company',__name__)

@company.route('/comphome',methods=['get','post'])
def comphome():
	return render_template('comphome.html')

@company.route('/company_predict',methods=['get','post'])
def company_predict():
	q = "select * from tbl_criteria"
	res = select(q)
	return render_template('company_predict.html',data=res)


@company.route('/company_result',methods=['get','post'])
def company_result():
	lid=session['loginid']
	q = "select * from tbl_criteria"
	res = select(q)
	input = []
	if "predict" in request.form:
		for i in range(len(res)):
			input.append(0)
		for row in res:
			name  = "criteria_" + str(row['criteria_id'])
			print(name)
			if name in request.form:
				level = float(request.form[name])
				criteria_id = row['criteria_id']
				input[criteria_id-1] = level
		result = core.predict(input,2)
		for row in result:
			q="insert into selection values(null,(select company_id from company where log_id='%s'),'%s',curdate(),'%s')" %(lid,row['student_id'],row['percent'])
			print(q)
			insert(q)
			print(result)
		return render_template('company_result.html',data = result)
	else:
		return render_template('company_predict.html')



@company.route('/result',methods=['get','post'])
def result():
	q = "select * from selection inner join student using(student_id) inner join course using(course_id)"
	res = select(q)
	return render_template('results.html',data=res)
