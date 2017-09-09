# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)

app.config.from_envvar('ICANTREAD_SETTINGS', silent=True)

@app.route('/')
def render_home():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def upload():
    return redirect(url_for('render_format_select'))

@app.route('/ezread')
def render_format_select():
    return render_template('fun_reading.html', type='facebook')

@app.route('/ezread', methods=['POST'])
def make_reading_fun():
    return render_template('feed.html')