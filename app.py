<<<<<<< HEAD
from flask import Flask, render_template
<<<<<<< HEAD

app = Flask(__name__)

=======
from markupsafe import escape
app = Flask(__name__)


>>>>>>> 3c0804ff114eef783dcdb5e6bc1c9e8c5242c04e
@app.route('/')
def index():
    return render_template('index.html')

<<<<<<< HEAD
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name="Dawid")

if __name__ == '__main__':
    app.run(debug=True)


=======

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
>>>>>>> 3c0804ff114eef783dcdb5e6bc1c9e8c5242c04e
=======
from flask import Flask, render_template
<<<<<<< HEAD

app = Flask(__name__)

=======
from markupsafe import escape
app = Flask(__name__)


>>>>>>> 3c0804ff114eef783dcdb5e6bc1c9e8c5242c04e
@app.route('/')
def index():
    return render_template('index.html')

<<<<<<< HEAD
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name="Dawid")

if __name__ == '__main__':
    app.run(debug=True)


=======

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
>>>>>>> 3c0804ff114eef783dcdb5e6bc1c9e8c5242c04e
>>>>>>> 9d688c3bff0d926265c8f3aa8d7c80ff71663b0a
