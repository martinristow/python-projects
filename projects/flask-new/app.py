from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    myvalue = "Martin Ristov"
    myresult = 10 + 20
    list = [10, 20, 30, 50, 80]
    return render_template('index.html', value=myvalue, result=myresult, list=list)


@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('other'))


@app.route('/other')
def other():
    text = 'Hello World'
    return render_template('other.html', text=text)


# custom filter made by me
@app.template_filter('alternate_case')
def alternate_case(c):
    return ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(c)])


# custom filter made by me
@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]


# custom filter made by me
@app.template_filter('repeat')
def repeat(s, times=2):
    return s * times


if __name__ == "__main__":
    app.run(debug=True)