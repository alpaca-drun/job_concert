from flask import Flask, render_template
from view.home import home_route

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

app.register_blueprint(home_route)

if __name__ == '__main__':
    app.run('localhost',port=5000,debug=True)

