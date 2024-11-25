from flask import Flask, jsonify, request
from config import get_db_connection

app = Flask(__name__)

# User Routes
@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM User")
    users = cursor.fetchall()
    conn.close()
    return jsonify(users)

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    query = "INSERT INTO User (Username, Email, Password, Bio) VALUES (%s, %s, %s, %s)"
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, (data['Username'], data['Email'], data['Password'], data['Bio']))
    conn.commit()
    conn.close()
    return jsonify({"message": "User added successfully!"})

# Post Routes
@app.route('/posts', methods=['GET'])
def get_posts():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Post")
    posts = cursor.fetchall()
    conn.close()
    return jsonify(posts)

@app.route('/add_post', methods=['POST'])
def add_post():
    data = request.json
    query = "INSERT INTO Post (UserID, Content) VALUES (%s, %s)"
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, (data['UserID'], data['Content']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Post created successfully!"})

# Comment Routes
@app.route('/comments', methods=['GET'])
def get_comments():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Comment")
    comments = cursor.fetchall()
    conn.close()
    return jsonify(comments)

@app.route('/add_comment', methods=['POST'])
def add_comment():
    data = request.json
    query = "INSERT INTO Comment (PostID, UserID, Content) VALUES (%s, %s, %s)"
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, (data['PostID'], data['UserID'], data['Content']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Comment added successfully!"})

# Like Routes
@app.route('/likes', methods=['GET'])
def get_likes():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Like")
    likes = cursor.fetchall()
    conn.close()
    return jsonify(likes)

@app.route('/add_like', methods=['POST'])
def add_like():
    data = request.json
    query = "INSERT INTO Like (PostID, UserID) VALUES (%s, %s)"
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, (data['PostID'], data['UserID']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Like added successfully!"})

# Message Routes
@app.route('/messages', methods=['GET'])
def get_messages():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Message")
    messages = cursor.fetchall()
    conn.close()
    return jsonify(messages)

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    query = "INSERT INTO Message (SenderID, ReceiverID, Content) VALUES (%s, %s, %s)"
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, (data['SenderID'], data['ReceiverID'], data['Content']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Message sent successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
