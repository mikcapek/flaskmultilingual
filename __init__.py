from flask import Flask, request, render_template, redirect, Blueprint, g, url_for
from flask_babelex import Babel, gettext, refresh
from config import Config

from app.blueprints.multilingual import multilingual



app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
app.register_blueprint(multilingual)


@babel.localeselector
def get_locale():
    if not g.get('lang_code', None):
        g.lang_code = request.accept_languages.best_match(app.config['LANGUAGES'])
    return g.lang_code

@app.route('/')
def home():
	g.lang_code = request.accept_languages.best_match(app.config['LANGUAGES'])
	return redirect(url_for('multilingual.index'))	

@app.route('/random')
def random():
	g.lang_code = request.accept_languages.best_match(app.config['LANGUAGES'])
	return redirect(url_for('multilingual.randomstuff'))	



if __name__ == '__main__':
	app.run(debug=True)