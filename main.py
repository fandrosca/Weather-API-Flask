#!/usr/bin/env python
from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for, jsonify
from weather import query_api

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'weather.html',
        data=[{'name':'London'}, {'name':'Paris'}, {'name':'Barcelona'},
        {'name':'Madrid'}, {'name':'Brussels'}, {'name':'Stockholm'},
        {'name':'Oslo'}, {'name':'Amsterdam'}, {'name':'Rome'},
        {'name':'Prague'}, {'name':'Bucharest'}, {'name':'Piatra Neamt'}])

@app.route("/weather" , methods=['GET', 'POST'])
def result():
    data = []
    error = None
    select = request.form.get('comp_select')
    resp = query_api(select)
    pp(resp)
    if resp:
       data.append(resp)
    if len(data) != 2:
        error = 'Bad Response from Weather API'
    return render_template('result.html',data=data,error=error)

@app.route("/rest/weather" , methods=['GET'])
def restresult():
    data = []
    error = None
    city =   request.args.get('city','Barcelona')
    resp = query_api(city)
    pp(resp)
    if resp:
       data.append(resp)
    if len(data) != 2:
        error = 'Bad Response from Weather API'
    return jsonify(resp)


if __name__=='__main__':
    app.run(debug=True)# ssl_context='adhoc')
