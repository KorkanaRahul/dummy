from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/about')
def about():
    return '''
    <h1>About This Project</h1>
    <p>This is a simple Flask web application deployed on Render.com.</p>
    <p>The purpose of this project is to demonstrate a basic deployment process 
    for a Python web application using Flask.</p>
    <p>The application contains a "Hello, World!" page and this introduction page.</p>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
