from database import *
import random
import pickle

from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier


def train():

	classifier = MLPClassifier()

	q = "select * from student"

	students = select(q)

	output = []

	criteria = select("select * from tbl_criteria order by criteria_id asc")

	training_ip = []

	for stud in students:
		ip = []
		for i in range(len(criteria)):
			ip.append(0)

		
		q = "select * from tbl_stud_criteria where stud_id='%s'" % (stud['student_id'])
		stud_cri = select(q)
		if(len(stud_cri) > 0):
			for cri in stud_cri:
				ip[int(cri['criteria_id'])-1] = float(cri['criteria_level'])
			# print(ip)
			# print(output)
			output.append(stud['student_id'])
			training_ip.append(ip)
	classifier.fit(training_ip,output)
	score = classifier.score(training_ip,output)
	file = open("classifier.pickle","wb")
	pickle.dump(classifier,file)
	file.close()
	return score

def predict(data,n):
	print(data)
	file = open("classifier.pickle","rb")
	classifier= pickle.load(file)
	op = classifier.predict([data])
	ar = classifier.predict_proba([data])
	print(ar)
	q = "select * from student order by student_id asc"
	res = select(q)
	result = {}
	i = 0
	# for row in res:
	# 	result[row['stud_id']] = ar[0][i]
	# 	i += 1
	zipped = zip(classifier.classes_,ar[0])
	sort = sorted(zipped, key=lambda value: value[1])
	sort = list(reversed(sort))
	

	r = []
	for i in range(len(sort)):
		r.append(str(sort[i][0]))
	q = "select * from student inner join course using(course_id) where student_id in %s" % ( "(" + ",".join(r) + ")" )
	res = select(q)
	sort = dict(sort)
	for i in range(len(res)):
		res[i]['percent'] = sort[res[i]['student_id']] * 100
	newlist = sorted(res, key=lambda k: k['percent'],reverse =True)
	return newlist




	


