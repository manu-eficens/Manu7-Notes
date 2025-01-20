from flask import Flask

app = Flask(__name__)  # Initialize the Flask application


@app.route("/")  # Define the route for the root URL
def hello_world():
    return "<p>Hello, World!</p>"  # Return a simple HTML response


if __name__ == '__main__':
    # Run the Flask app in debug mode and make it accessible on all network interfaces
    app.run(debug=True, host='0.0.0.0')
