from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        database=os.environ.get("DB_NAME", "anime_db"),
        user=os.environ.get("DB_USER", "user"),
        password=os.environ.get("DB_PASSWORD", "password")
    )

@app.route('/api/anime', methods=['GET'])
def get_anime():
    sample_data = [
        {"id": 1, "title": "Naruto", "genre": "Action"},
        {"id": 2, "title": "One Piece", "genre": "Adventure"},
        {"id": 3, "title": "Death Note", "genre": "Thriller"}
    ]
    return jsonify(sample_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
