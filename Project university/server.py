from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Crear base de datos
conn = sqlite3.connect('proximidad.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS estado (
        lugar TEXT PRIMARY KEY,
        color TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')
conn.commit()

@app.route('/estado', methods=['POST'])
def recibir_estado():
    data = request.get_json()
    lugar = data.get('lugar')
    color = data.get('color')
    cursor.execute('REPLACE INTO estado (lugar, color) VALUES (?, ?)', (lugar, color))
    conn.commit()
    return jsonify({'mensaje': 'Estado actualizado'}), 200


@app.route('/ver', methods=['GET'])
def ver_estado():
    cursor.execute('SELECT lugar, color FROM estado')
    datos = cursor.fetchall()
    return jsonify(datos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
