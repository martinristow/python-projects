from flask import Flask, render_template, redirect, url_for, request, Response, send_from_directory, jsonify, session
import pandas as pd
import os
import uuid
app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
app.secret_key = 'SOME KEY'


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', message='Index')


@app.route('/set_data')
def set_data():
    session['name'] = 'Mike'
    session['other'] = 'Hello World'
    return render_template('index.html', message='Session data set.')


@app.route('/get_data')
def get_data():
    if 'name' in session.keys() and 'other' in session.keys():
        name = session['name']
        other = session['other']
        return render_template('index.html', message=f'Name:{name}, other:{other}')
    else:
        return render_template('index.html', message='No session found')


@app.route('/clear_session')
def clear_session():
    session.clear()
    return render_template('index.html', message='Session cleared.')

if __name__ == "__main__":
    app.run(debug=True)