import os
import sqlite3
from flask import Flask, request, jsonify, send_from_directory

# Configuração de caminhos absolutos (Regra de Ouro)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "..", "database", "database.db")
PUBLIC_DIR = os.path.join(BASE_DIR, "..", "public")

app = Flask(__name__, static_folder=PUBLIC_DIR)

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# ==========================================
# Frontend Routes
# ==========================================
@app.route('/')
def index():
    return send_from_directory(PUBLIC_DIR, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(PUBLIC_DIR, path)

# ==========================================
# API Routes (Backend Lemuel)
# ==========================================

@app.route('/api/users', methods=['POST'])
def create_user():
    print("Recebendo cadastro de usuário...")
    data = request.json
    nome = data.get('nome')
    email = data.get('email')
    
    if not nome or not email:
        return jsonify({"error": "Nome e email são obrigatórios"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (nome, email) VALUES (?, ?)', (nome, email))
    conn.commit()
    user_id = cursor.lastrowid
    conn.close()
    
    print("Usuário salvo com sucesso")
    return jsonify({"id": user_id, "nome": nome, "email": email}), 201

@app.route('/api/stickers', methods=['POST'])
def add_sticker():
    print("Registrando figurinha...")
    data = request.json
    user_id = data.get('user_id')
    sticker_id = data.get('sticker_id') # Esperando sticker_id para simplificar
    
    if not user_id or not sticker_id:
        return jsonify({"error": "user_id e sticker_id são obrigatórios"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Verifica se já possui
    cursor.execute('SELECT id, quantidade FROM user_stickers WHERE user_id = ? AND sticker_id = ?', (user_id, sticker_id))
    row = cursor.fetchone()
    
    if row:
        nova_quantidade = row['quantidade'] + 1
        cursor.execute('UPDATE user_stickers SET quantidade = ?, is_repeated = 1 WHERE id = ?', (nova_quantidade, row['id']))
    else:
        cursor.execute('INSERT INTO user_stickers (user_id, sticker_id, quantidade, is_repeated) VALUES (?, ?, 1, 0)', (user_id, sticker_id))
        
    conn.commit()
    conn.close()
    
    print("Figurinha adicionada à coleção")
    return jsonify({"status": "success"}), 201

@app.route('/api/repeated', methods=['POST'])
def set_repeated():
    # Helper to explicitly mark repeated if needed
    data = request.json
    user_id = data.get('user_id')
    sticker_id = data.get('sticker_id')
    quantidade = data.get('quantidade', 2)

    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT id FROM user_stickers WHERE user_id = ? AND sticker_id = ?', (user_id, sticker_id))
    row = cursor.fetchone()
    
    if row:
        cursor.execute('UPDATE user_stickers SET quantidade = ?, is_repeated = 1 WHERE id = ?', (quantidade, row['id']))
    else:
        cursor.execute('INSERT INTO user_stickers (user_id, sticker_id, quantidade, is_repeated) VALUES (?, ?, ?, 1)', (user_id, sticker_id, quantidade))
        
    conn.commit()
    conn.close()
    return jsonify({"status": "success"}), 200

@app.route('/api/trades', methods=['POST'])
def create_trade():
    print("Criando proposta de troca...")
    data = request.json
    from_user_id = data.get('from_user_id')
    to_user_id = data.get('to_user_id')
    offered_sticker_id = data.get('offered_sticker_id')
    requested_sticker_id = data.get('requested_sticker_id')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO trades (from_user_id, to_user_id, offered_sticker_id, requested_sticker_id, status)
        VALUES (?, ?, ?, ?, 'pending')
    ''', (from_user_id, to_user_id, offered_sticker_id, requested_sticker_id))
    
    conn.commit()
    trade_id = cursor.lastrowid
    conn.close()
    
    print("Troca registrada")
    return jsonify({"id": trade_id, "status": "pending"}), 201

@app.route('/api/progress/<int:user_id>', methods=['GET'])
def get_progress(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 670 é o total estimado do album da Copa
    TOTAL_STICKERS = 670
    
    cursor.execute('SELECT COUNT(*) as collected FROM user_stickers WHERE user_id = ?', (user_id,))
    collected = cursor.fetchone()['collected']
    
    missing = TOTAL_STICKERS - collected
    completion_percentage = round((collected / TOTAL_STICKERS) * 100, 1) if TOTAL_STICKERS > 0 else 0
    
    conn.close()
    
    return jsonify({
        "user_id": user_id,
        "total_stickers": TOTAL_STICKERS,
        "collected": collected,
        "missing": missing,
        "completion_percentage": completion_percentage
    }), 200

if __name__ == '__main__':
    # Cria pasta database e banco caso não exista (segurança)
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    if not os.path.exists(DB_PATH):
        # Fallback caso init_db.py não tenha rodado
        print("Aviso: database.db não encontrado. Executando script de banco não é responsabilidade do app.py, mas prosseguindo...")
        
    app.run(host='0.0.0.0', port=5000, debug=True)
