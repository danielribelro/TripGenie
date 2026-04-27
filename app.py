import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from google import genai

app = Flask(__name__)

# --- CONFIGURAÇÃO ---
# Sua chave de API integrada
MINHA_CHAVE = "AIzaSyAqc8a4O5MVkfPzEAExMVR_mSTJ47b2aHU"
CLIENT = genai.Client(api_key=MINHA_CHAVE)
MODELO_NOME = "gemini-2.5-flash"

def get_db_connection():
    conn = sqlite3.connect('viagens.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS roteiros 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                     destino TEXT, hospedagem TEXT, itinerario TEXT)''')
    conn.commit()
    conn.close()

# --- ROTAS ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/historico')
def historico():
    conn = get_db_connection()
    viagens = conn.execute('SELECT * FROM roteiros ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('historico.html', viagens=viagens)

@app.route('/salvar', methods=['POST'])
def salvar():
    destino = request.form.get('destino')
    hospedagem = request.form.get('hospedagem')
    
    prompt = (
        f"Crie um roteiro objetivo de 2 dias para {destino} ficando no {hospedagem}. "
        "Não use introduções. Siga este formato estrito:\n"
        "DIA 1: [Titulo]\n- Manhã: [Atividade]\n- Tarde: [Atividade]\n- Noite: [Atividade]\n\n"
        "DIA 2: [Titulo]\n- Manhã: [Atividade]\n- Tarde: [Atividade]\n- Noite: [Atividade]"
    )

    try:
        response = CLIENT.models.generate_content(model=MODELO_NOME, contents=prompt)
        raw_text = response.text
        
        # Formatação de Timeline para o CSS Premium
        html_text = raw_text.replace("DIA 1", "<div class='day-section'><span class='day-badge'>DIA 01</span>")
        html_text = html_text.replace("DIA 2", "</div><div class='day-section'><span class='day-badge'>DIA 02</span>")
        html_text = html_text.replace("- Manhã:", "</div><div class='item'><strong>☀️ Manhã</strong><p>")
        html_text = html_text.replace("- Tarde:", "</p></div><div class='item'><strong>🌤️ Tarde</strong><p>")
        html_text = html_text.replace("- Noite:", "</p></div><div class='item'><strong>🌙 Noite</strong><p>")
        html_text += "</p></div>"
    except Exception as e:
        html_text = f"<div class='item'>Erro ao gerar: {e}</div>"

    conn = get_db_connection()
    conn.execute('INSERT INTO roteiros (destino, hospedagem, itinerario) VALUES (?, ?, ?)',
                 (destino, hospedagem, html_text))
    conn.commit()
    conn.close()
    return redirect(url_for('historico'))

@app.route('/deletar/<int:id>')
def deletar(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM roteiros WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('historico'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)