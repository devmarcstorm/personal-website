import datetime
import os

from flask import Flask  # pip install Flask
from flask import render_template
from flask import send_from_directory
from flask import request

from apps.portfolio.views import portfolio
from apps.utilities.files import read_from_file


app = Flask(__name__)
app.register_blueprint(portfolio, url_prefix='/')


@app.route('/media/<path:filename>')
def media(filename):
	return send_from_directory(f'{os.path.dirname(os.path.abspath(__file__))}/media', filename, as_attachment=True)


@app.errorhandler(404)
def page_not_found(e):
	try:
		content = read_from_file('content/content.json')
		page_info = content['pages']['404']
		mascot = read_from_file('content/mascot.txt')
		year = datetime.date.today().strftime("%Y")
		return render_template('error.html', page_info=page_info, tagline="Error 404", content=content, mascot=mascot, year=year), 404
	except KeyError:
		return r'<h1>404 Page not found :(</h1><a href="/">Home</a>'


@app.context_processor
def inject_now():
	"""Injects variables to all templates.
	
	Decorators:
		app.context_processor
	"""
	return {'year': datetime.date.today().strftime("%Y")}


@app.route('/robots.txt')
def get_static_file_from_root():
    return send_from_directory(app.static_folder, request.path[1:])