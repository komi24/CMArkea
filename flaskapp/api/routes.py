from flask import Blueprint
from api.user import user_api_routes


api_routes = Blueprint(name="api", import_name=__name__, url_prefix="/api")
api_routes.register_blueprint(user_api_routes)


@api_routes.route("/info")
def info():
    return {
        "version": "0.0.1",
        "author": "Mickael BOLNET",
        "email": "mickael.bolnet@gmail.com"
    }