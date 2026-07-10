from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/clientes")
"""
Esta rota serve para listar os clientes
"""
def listar_clientes():
    return jsonify(
        [
            {"id": 1, "nome": "Ana Lima", "email": "ana@example.com"},
            {"id": 2, "nome": "Bruno Costa", "email": "bruno@example.com"},
        ]
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
