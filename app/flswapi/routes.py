from flask import request, jsonify
from flask_restplus import Resource

from app.flswapi import api
from app.flswapi.models import User, users_schema, model


@api.route("/api/get_users")
class GetUser(Resource):
    def get(self):
        data = User.query.all()
        return jsonify(users_schema.dump(data))


@api.route("/api/put_user/<int:id>")
class AddUser(Resource):
    @api.expect(model)
    def put(self, id):
        # user = User.query.get(id)
        # user.login = request.json['login']
        # user.password = request.json['password']
        # db.session.commit()
        return {'message': 'user added'}


@api.route("/api/post_user")
class PostUser(Resource):
    @api.expect(model)
    def post(self):
        # user = User(login=request.json['login'], password=request.json['password'])
        # db.session.add(user)
        # db.session.commit()
        return {'message': 'Success'}


@api.route("/api/delete_user/<int:id>")
class DeleteUser(Resource):
    def delete(self,id):
        # user = User.query.get(id)
        # db.session.delete(user)
        # db.session.commit()
        return {'message': 'user deleted'}
