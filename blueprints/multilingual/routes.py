from flask import render_template, Blueprint, g, redirect, request, current_app, abort, url_for
# from app import app

multilingual = Blueprint('multilingual', __name__, template_folder='templates', url_prefix='/<lang_code>')



@multilingual.url_defaults
def add_language_code(endpoint, values):
	values.setdefault('lang_code', g.lang_code)

@multilingual.url_value_preprocessor
def pull_lang_code(endpoint, values):
	g.lang_code = values.pop('lang_code')

@multilingual.route('/')
@multilingual.route('/index')
def index():
	return render_template('multilingual/index.html', title='Home')
