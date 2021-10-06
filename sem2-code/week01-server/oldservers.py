from flask import Flask, render_template

app = Flask(__name__, static_url_path='', static_folder='staticpages')


@app.route('/user/<name>')
def user(name):
    return render_template('hello.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)
