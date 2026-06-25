import json
import os
from flask import Flask, jsonify

app = Flask(__name__)


def carregar_fotos():
    caminho = os.path.join(os.path.dirname(__file__), 'data', 'fotos.json')
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)


@app.route('/status')
def status():
    return jsonify({
        "nome": "FotoSocial API",
        "versao": "1.0.0",
        "status": "ok"
    }), 200


@app.route('/fotos')
def listar_fotos():
    try:
        fotos = carregar_fotos()
        return jsonify({
            "total": len(fotos),
            "fotos": fotos
        }), 200
    except Exception:
        return jsonify({"erro": "Falha ao carregar as fotos"}), 500


@app.route('/fotos/<int:foto_id>')
def buscar_foto(foto_id):
    try:
        fotos = carregar_fotos()
        foto = next((f for f in fotos if f['id'] == foto_id), None)

        if foto is None:
            return jsonify({"erro": f"Foto {foto_id} não encontrada"}), 404

        return jsonify(foto), 200
    except Exception:
        return jsonify({"erro": "Erro interno"}), 500


if __name__ == '__main__':
    app.run(debug=True)