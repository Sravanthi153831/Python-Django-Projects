from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)
DB_NAME = "smart_factory.db"

# 1. Security Logic for Korean Tech Standards
def check_auth(username, password):
    return username == 'korea_admin' and password == 'password123'

# 2. Database Initialization for Smart Factory
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

# 3. GET Method - Fetch all factory assets
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
            "item_id": row[0],          # ఇండెక్స్ 0 ఉపయోగించి ID ని తీసుకున్నాం
            "item_name": row[1],        # ఇండెక్స్ 1 లో నేమ్ వస్తుంది
            "robot_assigned": row[2],   # ఇండెక్స్ 2 లో రోబోట్ వివరాలు
            "status": row[3]            # ఇండెక్స్ 3 లో స్టేటస్ వస్తుంది
        })
    return jsonify(items), 200

# 4. POST Method - Register a new item placed by robot
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

# 5. PUT Method - Update item status by Robot ID
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
    return jsonify({"status": "success", "message": "Item status updated"}), 200

# 6. DELETE Method - Remove dispatched item from DB
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
    return jsonify({"status": "success", "message": "Item deleted from database"}), 200

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
