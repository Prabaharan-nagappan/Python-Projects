from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! this is sample website'

@app.route('/about')
def about():
    return 'About page'



if __name__ == '__main__':
    app.run(debug=True)
