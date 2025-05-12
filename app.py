from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# In-memory variable to store the greeting message
greeting = "Hello, World!"

# CREATE - Add or set a new greeting
@app.route('/hello', methods=['POST'])
def create_greeting():
    global greeting
    # Get JSON data from the request body
    data = request.get_json()
    # Set the greeting to the provided value or default if not provided
    greeting = data.get('greeting', "Hello, World!")
    # Return a response with the new greeting
    return jsonify({"message": "Greeting created", "greeting": greeting}), 201

# READ - Get the current greeting
@app.route('/hello', methods=['GET'])
def read_greeting():
    # Return the current greeting as JSON
    return jsonify({"greeting": greeting})

# UPDATE - Update the greeting
@app.route('/hello', methods=['PUT'])
def update_greeting():
    global greeting
    # Get JSON data from the request body
    data = request.get_json()
    # Update the greeting with the new value, or keep the old one if not provided
    greeting = data.get('greeting', greeting)
    # Return a response with the updated greeting
    return jsonify({"message": "Greeting updated", "greeting": greeting})

# DELETE - Delete the greeting (set to empty string)
@app.route('/hello', methods=['DELETE'])
def delete_greeting():
    global greeting
    # Set the greeting to an empty string
    greeting = ""
    # Return a response confirming deletion
    return jsonify({"message": "Greeting deleted"})

# Run the Flask development server if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)