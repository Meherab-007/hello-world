from flask import Flask, render_template

app = Flask(__name__)
app.template_folder = 'templates'

our_message = "Hello world."


@app.route('/')
def hello_world():
    return render_template('index.html', message=our_message)


if __name__ == '__main__':
    app.run(debug=True)
