from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)
DB_NAME = "smart_factory.db"

# 1. Security Logic for Korean Tech Standards
def check_auth(username, password):
    return username == 'korea_admin' and password == 'seoul2026'

# 2. Database Initialization for Smart Factory Inventory
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

# 3. GET Method - Fetch all factory assets (Secured)
@app.route('/factory/items', methods=['GET'])
def get_factory_items():
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return jsonify({"status": "error", "message": "Access Denied! Invalid Credentials."}), 401

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM inventory')
    rows = cursor.fetchall()
    conn.close()
    
    items = []
    for row in rows:
        items.append({
            "item_id": row,
            "item_name": row,
            "robot_assigned": row,
            "status": row
        })
    return jsonify(items), 200

# 4. POST Method - Register a new item placed by a Robot (Secured)
@app.route('/factory/items', methods=['POST'])
def add_factory_item():
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return jsonify({"status": "error", "message": "Access Denied! Invalid Credentials."}), 401
        
    data = request.get_json()
    if not data or 'item_name' not in data or 'robot_assigned' not in data:
        return jsonify({"status": "error", "message": "Missing item_name or robot_assigned!"}), 400
        
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO inventory (item_name, robot_assigned) VALUES (?, ?)', 
                   (data['item_name'], data['robot_assigned']))
    conn.commit()
    conn.close()
    
    return jsonify({"status": "success", "message": "Item registered by Robot successfully!"}), 201

# 5. PUT Method - Update item status by Robot ID (Secured)
@app.route('/factory/items/<int:item_id>', methods=['PUT'])
def update_item_status(item_id):
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return jsonify({"status": "error", "message": "Access Denied! Invalid Credentials."}), 401
        
    data = request.get_json()
    new_status = data.get('status', 'Dispatched')
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('UPDATE inventory SET status = ? WHERE item_id = ?', (new_status, item_id))
    conn.commit()
    
    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"status": "error", "message": "Item Asset not found!"}), 404
        
    conn.close()
    return jsonify({"status": "success", "message": f"Item {item_id} status updated to {new_status}!"}), 200

# 6. DELETE Method - Remove dispatched item from warehouse database (Secured)
@app.route('/factory/items/<int:item_id>', methods=['DELETE'])
def delete_factory_item(item_id):
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return jsonify({"status": "error", "message": "Access Denied! Invalid Credentials."}), 401
        
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM inventory WHERE item_id = ?', (item_id,))
    conn.commit()
    
    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"status": "error", "message": "Item Asset not found!"}), 404
        
    conn.close()
    return jsonify({"status": "success", "message": f"Item {item_id} removed from factory database!"}), 200

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
