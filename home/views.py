import os
from tay_flask import app
from flask import render_template, redirect, session, request, url_for, json

@app.route('/')
@app.route('/index')
def index():
	return "Hello World"
