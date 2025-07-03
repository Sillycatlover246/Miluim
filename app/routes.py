from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/salary')
def salary():
    return render_template('salary.html')

@main.route('/grant')
def grant():
    return render_template('grant.html')

@main.route('/refunds')
def refunds():
    return render_template('refunds.html')
