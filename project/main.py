from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db
from .generator import generate_market_data_for_our_pairs
from .data import generate_data_for_web, markets

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    data_dict_for_web = generate_market_data_for_our_pairs(generate_data_for_web())
    return render_template('profile.html', data=data_dict_for_web, markets=markets, name=current_user.name)
