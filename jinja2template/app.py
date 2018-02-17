#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from flask import Flask, render_template

app=Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']=True
#with this you don't have to restart the server every time you change app.py or templates, and only have to refresh the page
#in shell type the following to run: FLASK_DEBUG = 1 FLASK_APP=app.py flask run port 5000. port 5000 is optional

#add filter
def hide_email(email):
	parts=email.split('@')
	parts[0]='***'
	return '@'.join(parts)

app.add_template_filter(hide_email)

@app.route('/')
def index():
	teacher={
		'name': 'Aiden',
		'email': 'luojing@simplecloud.cn'
	}
	course={
	'name': 'Python Basic',
	'teacher': teacher,
	'user_count': 5348,
	'price': 199,
	'lab': None,
	'is_private': False,
	'is_member_course': True,
	'tags': ['Python','Linux','bigdata']
	}
	return render_template('index.html',course=course)
