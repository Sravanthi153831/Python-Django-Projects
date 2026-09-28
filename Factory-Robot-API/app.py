from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)
DB_NAME = "smart_factory.db"

# 1. Security Verification for Admin Access
def check_auth(username, password):
    return username == 'korea_admin' and password == 'password123'

# 2. Database Initialization and Table Creation
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            item_id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL,
            robot_assigned TEXT NOT NULL,
            status TEXT DEFAULT 'Stored'
        )
    ''')
    conn.commit()
    conn.close()

# 3. GET Method - Fetch all factory assets from the database
@app.route('/factory/items', methods=['GET'])
def get_factory_items():
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return jsonify({"status": "error", "message": "Unauthorized access"}), 401
        
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT item_id, item_name, robot_assigned, status FROM inventory')
    rows = cursor.fetchall()
    conn.close()
    
    items = []
    for row in rows:
        items.append({
            "item_id": row[0],
            "item_name": row[1],
            "robot_assigned": row[2],
            "status": row[3]
        })
    return jsonify(items), 200

# 4. POST Method - Register a new factory item placed by a robot
@app.route('/factory/items', methods=['POST'])
def add_factory_item():
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return jsonify({"status": "error", "message": "Unauthorized access"}), 401
        
    data = request.get_json()
    if not data or 'item_name' not in data or 'robot_assigned' not in data:
        return jsonify({"status": "error", "message": "Missing required fields"}), 400
        
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO inventory (item_name, robot_assigned, status) VALUES (?, ?, ?)',
        (data['item_name'], data['robot_assigned'], data.get('status', 'Stored'))
    )
    conn.commit()
    conn.close()
    
    return jsonify({"status": "success", "message": "Robot item registered successfully"}), 201

# 5. PUT Method - Update item status using specific Item ID
@app.route('/factory/items/<int:item_id>', methods=['PUT'])
def update_item_status(item_id):
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return jsonify({"status": "error", "message": "Unauthorized access"}), 401
        
    data = request.get_json()
    new_status = data.get('status', 'Dispatched')
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('UPDATE inventory SET status = ? WHERE item_id = ?', (new_status, item_id))
    conn.commit()
    
    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"status": "error", "message": "Item not found"}), 404
        
    conn.close()
    return jsonify({"status": "success", "message": "Item status updated successfully"}), 200

# 6. DELETE Method - Remove an item from the database
@app.route('/factory/items/<int:item_id>', methods=['DELETE'])
def delete_factory_item(item_id):
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return jsonify({"status": "error", "message": "Unauthorized access"}), 401
        
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM inventory WHERE item_id = ?', (item_id,))
    conn.commit()
    
    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"status": "error", "message": "Item not found"}), 404
        
    conn.close()
    return jsonify({"status": "success", "message": "Item deleted from database successfully"}), 200

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
