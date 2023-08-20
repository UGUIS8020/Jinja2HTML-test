# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', index = True, title = 'index.html')

@app.route('/prev/')
def prev():
	return render_template('prev.html', prev = True, title = 'prev.html')

@app.route('/next/')
def next():
	return render_template('next.html', next = True, title = 'next.html')