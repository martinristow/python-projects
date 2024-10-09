from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>zdr</h1>"


@app.route('/hello', methods=['POST', 'GET'])
def hello():
    if request.method == 'GET':
        return 'You made a GET request\n'
    elif request.method == 'POST':
        return 'You made a POST request\n'
    else:
        return 'You will never see this message\n'


@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}"


@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    return f"{number1} + {number2} = {number2+number1}"


@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args.get('greeting')
        name = request.args.get('name')
        return f'{greeting}, {name}'
    else:
        return 'Some parameters are missing!'



if __name__ == "__main__":
    app.run(debug=True)