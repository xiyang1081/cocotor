# -*- coding: utf-8 -*-

# import MySQLdb
from flask import Flask, g, request, render_template

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('mysite/error/404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('mysite/error/500.html'), 500


if __name__ == '__main__':
    app.run()
