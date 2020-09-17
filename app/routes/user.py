from app.models.models import db, User
from flask_restx import Resource, Namespace, fields
from flask_jwt_extended import ( jwt_required, get_jwt_identity)

api = Namespace('user', description='Create and update user operations')

model = api.model("User", {
                            "firstName": fields.String( description="User first name.", example="John"),
                            "lastName": fields.String( description="User last name.", example="Doe"),
                            "userInfo": fields.String( description="User information.", example = "I love the oudoors"),
                            "domicileType": fields.String( description="User domicile type.", example = "RV"),
                            "phoneNumber": fields.String( description="User phone number.", example="555-555-5555"),
                            "password": fields.String( description="User Password.", example="password"),
                            "imageURL": fields.String( description="User Image URL.", example="/image.png"),
                         }
                )

@api.route("/<int:id>")
@api.param('id', 'User identifier')
@api.response(404, 'User not found')
@api.param('id', 'The user identifier')
class GetUser(Resource):
    @api.response(200, 'User found')
    @api.doc('get_user')
    def get(self, id):
        '''Get user by user id'''
        user = User.query.get(int(id))
        if user == None:
            return {"message": "no user found for the requested id"}, 404

        return {"user":user.to_dictionary()}

@api.route("/")
class UserAccount(Resource):
    @api.response(200, 'User found')
    @api.doc('get_user')
    @jwt_required
    def get(self):
        '''Get user by using the passed in access token in the payload, obtained on a user authorization'''
        userId = get_jwt_identity()

        if userId == None:
            return {"message": "Not a valid user access token send "}, 404

        user = User.query.get(userId)
        if user == None:
            return {"message": "no user found for the requested id"}, 404

        return {"user":user.to_dictionary()}


    @api.doc('update_user')
    @api.response(201, 'User record updated')
    @api.expect(model)
    @jwt_required
    def put(self):
        '''Update user record by user'''
        userId = get_jwt_identity()

        if userId == None:
            return {"message": "Not a valid user access token send "}, 404

        user = User.query.get(userId)
        if user == None:
            return {"message": "no user found for the requested id"}

        user.image_url = api.payload["imageURL"]
        user.phone_number = api.payload["phoneNumber"]
        user.user_info = api.payload["userInfo"]
        user.domicile_type = api.payload["domicileType"]
        user.first_name = api.payload["firstName"]
        user.last_name = api.payload["lastName"]
        db.session.commit()

        return {"message": "User record updated successfully."}
