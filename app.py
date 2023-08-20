# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', title = 'index.html')

@app.route('/prev/')
def prev():
	return render_template('prev.html', title = 'prev.html')

@app.route('/next/')
def next():
	return render_template('next.html', title = 'next.html')