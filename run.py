from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Agilus'

if __name__ == '__main__':
    app.run()
