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
def make_reading_fun():
    return 'sup'