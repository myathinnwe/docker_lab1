# Import the Flask module
from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route and its corresponding function
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the application if the script is executed
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
