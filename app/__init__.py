from flask import Flask, request, render_template, redirect, Blueprint
from flask_babelex import Babel, gettext

from app.blueprints.multilingual import multilingual


app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)
app.register_blueprint(multilingual)

@babel.localeselector
def get_locale():
	if request.args.get('lang'):
		session['lang'] = request.args.get('lang')
		return session.get('lang', 'en')

@app.route('/')
def index():

	whatever = gettext('Hi from Prague')

	return render_template('index.html', whatever= whatever)

if __name__ == '__main__':
	app.run(debug=True)