from flask import render_template, Blueprint
from flaskmultilingual import app

multilingual = Blueprint('multilingual', __name__, template_folder='templates')

@multilingual.route('/')
def index():
	return render_template('multilingual/index.html', title='Home')
