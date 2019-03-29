#!/usr/bin/env python
#import libraries
from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for, jsonify
from weather import query_api

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'weather.html',     #HTML template
        data=[{'name':'London'}, {'name':'Paris'}, {'name':'Barcelona'},
        {'name':'Madrid'}, {'name':'Brussels'}, {'name':'Stockholm'},
        {'name':'Oslo'}, {'name':'Amsterdam'}, {'name':'Rome'},
        {'name':'Prague'}, {'name':'Bucharest'}, {'name':'Piatra Neamt'}]) #cities in the drop-down list

#GET and POST methods
@app.route("/weather" , methods=['GET', 'POST'])
def result():
    data = []
    error = None
    select = request.form.get('comp_select')
    resp = query_api(select) #function defined in weather.py
    pp(resp)
    if resp:
       data.append(resp)
    if len(data) != 2:
        error = 'Bad Response from Weather API' #response in case of malformed data
    return render_template('result.html',data=data,error=error) #return the result using the HTML template

#RESTful API - GET
@app.route("/rest/weather" , methods=['GET'])
def restresult():
    data = []
    error = None
    city =   request.args.get('city','Barcelona') #arguments
    resp = query_api(city) #function defined in weather.py
    pp(resp)
    if resp:
       data.append(resp)
    if len(data) != 2:
        error = 'Bad Response from Weather API' #response in case of malformed data
    return jsonify(resp) #response in JSON format


if __name__=='__main__':
    app.run(debug=True) # ssl_context='adhoc'
