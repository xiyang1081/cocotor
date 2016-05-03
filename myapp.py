# -*- coding: utf-8 -*-

# import MySQLdb
from flask import Flask, g, request, render_template

app = Flask(__name__)
app.debug = True

# from sae.const import (MYSQL_HOST, MYSQL_HOST_S,
#     MYSQL_PORT, MYSQL_USER, MYSQL_PASS, MYSQL_DB
# )

# @app.before_request
# def before_request():
#     g.db = MySQLdb.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASS,
#                            MYSQL_DB, port=int(MYSQL_PORT))

# @app.teardown_request
# def teardown_request(exception):
#     if hasattr(g, 'db'): g.db.close()

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