# 🪄 TripGenie - Seu Assistente de Viagens

O **TripGenie** é uma aplicação web desenvolvida em Python com Flask, projetada para ajudar usuários a planejar e gerenciar suas viagens de forma inteligente e organizada.

## 🚀 Funcionalidades
* **Planejamento de Roteiros:** Organize seus destinos e datas de viagem.
* **Gestão de Banco de Dados:** Armazenamento seguro de informações de viagens utilizando SQLite.
* **Interface Responsiva:** Frontend limpo e intuitivo utilizando Jinja2 (templates HTML) e CSS.
* **Integração Backend-Frontend:** Comunicação fluida entre a lógica de servidor em Python e a interface do usuário.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python
* **Framework Web:** Flask
* **Banco de Dados:** SQLite
* **Frontend:** HTML5, CSS3 e Jinja2
* **Servidor de Produção:** Gunicorn (para deploy no Render)

## 📦 Como rodar o projeto localmente
1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/danielribelro/TripGenie.git](https://github.com/danielribelro/TripGenie.git)
   cd TripGenie
   
2. **Crie um ambiente virtual:**
```Bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

3. **Instale as dependências:**
```Bash
pip install -r requirements.txt
Execute a aplicação:

4. **Execute a aplicação:**
```Bash
python app.py
Acesse o projeto em: http://127.0.0.1:5000

🌐 Hospedagem (Deploy)
Este projeto está configurado para ser hospedado no Render.

Build Command: pip install -r requirements.txt

Start Command: gunicorn app:app

📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

Desenvolvido por Daniel Ribeiro
