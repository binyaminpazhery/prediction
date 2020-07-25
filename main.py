from flask import *
from public import public
from admin import admin
from employee import employee
from company import company
app=Flask(__name__)
app.secret_key="dfghj"
app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(employee,url_prefix='/employee')
app.register_blueprint(company,url_prefix='/company')
app.run(debug=True,port=5001)