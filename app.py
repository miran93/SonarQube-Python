from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated database of users
users = [
    {"id": 1, "name": "A", "email": "abc@example.com"},
    {"id": 2, "name": "B", "email": "xyz@example.com"}
]

@app.route('/')
def index():
    return "Welcome to the User API!"

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user is not None:
        return jsonify(user)
    else:
        return "User not found", 404

@app.route('/user', methods=['POST'])
def add_user():
    # Intentional potential security vulnerability (use of eval)
    user = eval(request.data)
    users.append(user)
    return jsonify(user), 201

# Unused method - example of dead code
def unused_method():
    print("This method is never used.")

if __name__ == "__main__":
    app.run(debug=True)
