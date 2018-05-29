#!/usr/bin/env python3.5
# -*- coding:utf-8 -*-

from flask import Flask, render_template, request, g, session, url_for, redirect, flash
from flask_bootstrap import Bootstrap
 

app = Flask(__name__)
app.config.from_object('config')
app.config.from_object('secret_config')


 
@app.route('/')
def index () :
    return render_template('accueil.html')


if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0') 