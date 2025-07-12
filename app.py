from flask import Flask, request, jsonify, abort
from models import db, Condominio, Appartamento


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///condominio.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    @app.before_first_request
    def create_tables():
        db.create_all()

    @app.route('/condomini', methods=['GET'])
    def list_condomini():
        condomini = Condominio.query.all()
        return jsonify([
            {'id': c.id, 'nome': c.nome, 'indirizzo': c.indirizzo}
            for c in condomini
        ])

    @app.route('/condomini/<int:condominio_id>', methods=['GET'])
    def get_condominio(condominio_id):
        condominio = Condominio.query.get_or_404(condominio_id)
        return jsonify({'id': condominio.id, 'nome': condominio.nome, 'indirizzo': condominio.indirizzo})

    @app.route('/condomini', methods=['POST'])
    def create_condominio():
        data = request.get_json()
        if not data or not all(k in data for k in ('nome', 'indirizzo')):
            abort(400, 'Nome e indirizzo sono obbligatori')
        condominio = Condominio(nome=data['nome'], indirizzo=data['indirizzo'])
        db.session.add(condominio)
        db.session.commit()
        return jsonify({'id': condominio.id}), 201

    @app.route('/appartamenti', methods=['POST'])
    def create_appartamento():
        data = request.get_json()
        required = ('condominio_id', 'numero', 'proprietario')
        if not data or not all(k in data for k in required):
            abort(400, 'Dati mancanti')
        condominio = Condominio.query.get_or_404(data['condominio_id'])
        appartmento = Appartamento(
            numero=data['numero'], proprietario=data['proprietario'], condominio=condominio
        )
        db.session.add(appartmento)
        db.session.commit()
        return jsonify({'id': appartmento.id}), 201

    return app


if __name__ == '__main__':
    application = create_app()
    application.run(debug=True)
