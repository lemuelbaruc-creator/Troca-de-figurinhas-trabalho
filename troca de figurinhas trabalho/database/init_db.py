import sqlite3
import os

# Caminho absoluto para o banco de dados
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")

def init_db():
    print(f"Inicializando banco de dados em {DB_PATH}...")
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Tabela: users
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Tabela: stickers
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS stickers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo TEXT NOT NULL,
        nome TEXT NOT NULL,
        time TEXT NOT NULL
    )
    ''')

    # Tabela: user_stickers
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_stickers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        sticker_id INTEGER NOT NULL,
        quantidade INTEGER DEFAULT 1,
        is_repeated BOOLEAN DEFAULT 0,
        FOREIGN KEY (user_id) REFERENCES users (id),
        FOREIGN KEY (sticker_id) REFERENCES stickers (id)
    )
    ''')

    # Tabela: trades
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS trades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        from_user_id INTEGER NOT NULL,
        to_user_id INTEGER NOT NULL,
        offered_sticker_id INTEGER NOT NULL,
        requested_sticker_id INTEGER NOT NULL,
        status TEXT DEFAULT 'pending',
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (from_user_id) REFERENCES users (id),
        FOREIGN KEY (to_user_id) REFERENCES users (id),
        FOREIGN KEY (offered_sticker_id) REFERENCES stickers (id),
        FOREIGN KEY (requested_sticker_id) REFERENCES stickers (id)
    )
    ''')

    # Inserir mock de figurinhas da Copa
    cursor.execute("SELECT COUNT(*) FROM stickers")
    if cursor.fetchone()[0] == 0:
        print("Inserindo figurinhas iniciais...")
        stickers_mock = [
            ("#15", "Neymar", "Brasil"),
            ("#87", "Vinicius Jr", "Brasil"),
            ("#310", "Messi", "Argentina"),
            ("#88", "Mbappé", "França"),
            ("#412", "Bellingham", "Inglaterra"),
            ("#10", "Pelé", "Lendas"),
            ("#7", "Cristiano Ronaldo", "Portugal")
        ]
        cursor.executemany("INSERT INTO stickers (codigo, nome, time) VALUES (?, ?, ?)", stickers_mock)
        
    conn.commit()
    conn.close()
    
    print("Banco de dados inicializado com sucesso!")

if __name__ == "__main__":
    init_db()
