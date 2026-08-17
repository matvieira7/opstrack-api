from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "service": "OpsTrack API",
        "status": "online"
    })


@app.route("/status")
def status():
    return jsonify({
        "status": "online"
    })


@app.route("/tickets")
def tickets():
    return jsonify([
        {
            "id": 1,
            "titulo": "Erro no login",
            "status": "aberto"
        },
        {
            "id": 2,
            "titulo": "Problema no sistema",
            "status": "em andamento"
        },
        {
            "id": 3,
            "titulo": "Solicitacao de acesso",
            "status": "fechado"
        }
    ])


#teste do diff
if __name__ == "__main__":
    app.run(debug=True)