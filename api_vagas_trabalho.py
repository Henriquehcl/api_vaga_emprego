from flask import Flask, request
from flask_restful import Resource, Api
from model_db import Vagas

app = Flask(__name__)
api = Api(app)


class Vaga(Resource):
    def get(self, vaga_id):
        try:
            vaga = Vagas.query.filter_by(vaga_id=vaga_id).first()
            response = {
                'id': vaga.vaga_id,
                'titulo': vaga.titulo,
                'descricao': vaga.descricao,
                'salario': vaga.salario,
                'empresa': vaga.empresa,
                'contratacao': vaga.contratacao,
                'modalidade': vaga.modalidade
            }
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'vaga não encontrada'
            }
        return response

    def put(self, vaga_id):
        try:
            vaga = Vagas.query.filter_by(vaga_id=vaga_id).first()
            dados = request.json

            vaga.titulo = dados['titulo']
            vaga.descricao = dados['descricao']
            vaga.salario = dados['salario']
            vaga.empresa = dados['empresa']
            vaga.contratacao = dados['contratacao']
            vaga.modalidade = dados['modalidade']
            vaga.save()
            response = {
                'id': vaga.vaga_id,
                'titulo': vaga.titulo,
                'descricao': vaga.descricao,
                'salario': vaga.salario,
                'empresa': vaga.empresa,
                'contratacao': vaga.contratacao,
                'modalidade': vaga.modalidade
            }
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'vaga não encontrada para fazer a edição'
            }

        return response

    def delete(self, vaga_id):
        try:
            vaga = Vagas.query.filter_by(vaga_id=vaga_id).first()
            response = {'status': 'sucesso', 'mensagem': 'Vaga {} excluída com sucesso'.format(vaga.titulo)}
            vaga.delete()
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'vaga não encontrada para fazer a exclusão'
            }
        return response


class ListaVagas(Resource):
    def get(self):
        try:
            vagas = Vagas.query.all()
            response = [{
                'id': i.vaga_id,
                'titulo': i.titulo,
                'descricao': i.descricao,
                'salario': i.salario,
                'empresa': i.empresa,
                'contratacao': i.contratacao,
                'modalidade': i.modalidade
            } for i in vagas]
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'não foi possível executar a consulta. Se o erro persisitir, contate o administrador'
            }
        return response

    def post(self):
        try:
            dados = request.json
            vaga = Vagas(
                titulo=dados['titulo'],
                descricao=dados['descricao'],
                salario=dados['salario'],
                empresa=dados['empresa'],
                contratacao=dados['contratacao'],
                modalidade=dados['modalidade']
            )
            vaga.save()
            response = {
                'id': vaga.vaga_id,
                'titulo': vaga.titulo,
                'descricao': vaga.descricao,
                'salario': vaga.salario,
                'empresa': vaga.empresa,
                'contratacao': vaga.contratacao,
                'modalidade': vaga.modalidade
            }
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'não foi possível fazer o cadastro. Se o erro persisitir, contate o administrador'
            }
        return response


api.add_resource(Vaga, '/<int:vaga_id>')
api.add_resource(ListaVagas, '/')


if __name__ == '__main__':
    app.run(debug=True)
