from flask import Flask, render_template

app = Flask(__name__)


@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=2)


@app.route('/training/<prof>')
def train(prof):
    return render_template('training.html', profession=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')