# Weather-API-Flask


## What is flask-weather-app?

It is an application built as coursework for the Cloud Computing module at Queen Mary University of London, part of the Big Data Science programme..

It uses Python, Flask, HTML, and CSS to illustrate core computer science concepts like APIs and requests.


## What do I need to run the application?

Assuming you already have Flask installed, if not go here (http://flask.pocoo.org/) or if you don't feel like reading just run this command:

```
pip install -U Flask
```

Use of virtualenv is encouraged.

You also need an OpenWeatherMap API key. You can get it at the following http://openweathermap.org/appid#get.

## Getting Started

First, begin by cloning this repo to your local machine:
```
$ git clone https://github.com/.../Weather-API-Flask.git <YOUR_DIR_NAME>
```

Next, create and source a virtual environment so that you can install the requirements for this project. Using Python's virtualenv tool is recommended.
```
$ virtualenv venv
$ source env/bin/activate
```

After sourcing your virtual environment, you can use pip to install the requirements. Please check out the pip documentation for instructions on usage.
```
(venv) $ pip install -r requirements.txt
```

## Running the app
Once all required packages have finished installing and you have sourced your key, you will be ready to run the application locally using:
```
(venv) $ python server.py
```
Visit localhost:5000 in the browser of your choice to make weather queries.
