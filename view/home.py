from flask import Blueprint, render_template

home_route = Blueprint('test',__name__)

@home_route.route('/test')
def test():
    return render_template('test.html')