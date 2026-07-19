from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)
DB_NAME = "todo_project.db"

# 1. Database Setup - Creates table automatically if it doesn't exist
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            status TEXT DEFAULT 'Pending'
        )
    ''')
    conn.commit()
    conn.close()

# 2. GET Method - Fetch all tasks from database
@app.route('/todos', methods=['GET'])
def get_todos():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM todos')
    rows = cursor.fetchall()
    conn.close()
    
    todo_list = []
    for row in rows:
        todo_list.append({
            "id": row[0],
            "title": row[1],
            "status": row[2]
        })
    return jsonify(todo_list), 200

# 3. POST Method - Add a new task to the database
@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({"status": "error", "message": "Title is required!"}), 400
        
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO todos (title) VALUES (?)', (data['title'],))
    conn.commit()
    conn.close()
    
    return jsonify({"status": "success", "message": "Task added to project database!"}), 201

# 4. PUT Method - Update a specific task status using its ID in URL
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.get_json()
    new_status = data.get('status', 'Completed')
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('UPDATE todos SET status = ? WHERE id = ?', (new_status, todo_id))
    conn.commit()
    
    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"status": "error", "message": "Task not found!"}), 404
        
    conn.close()
    return jsonify({"status": "success", "message": f"Task {todo_id} updated to {new_status}!"}), 200

# 5. DELETE Method - Delete a specific task using its ID in URL
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM todos WHERE id = ?', (todo_id,))
    conn.commit()
    
    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"status": "error", "message": "Task not found!"}), 404
        
    conn.close()
    return jsonify({"status": "success", "message": f"Task {todo_id} deleted successfully!"}), 200

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
