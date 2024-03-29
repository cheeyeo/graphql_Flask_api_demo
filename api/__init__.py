import os
from flask import Flask
from flask import request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from ariadne import load_schema_from_path, make_executable_schema, graphql_sync, snake_case_fallback_resolvers, QueryType, ObjectType
from ariadne.explorer import ExplorerGraphiQL
from api.database import DB
from api.queries import list_posts_resolver, get_post_resolver
from api.mutations import create_post_resolver, update_post_resolver, delete_post_resolver
from api.database import Post


app = Flask(__name__)
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')

# Setup db
DB.init_app(app)

with app.app_context():
    DB.create_all()


# Setup CORS
CORS(app)

# Setup graphql
type_defs = load_schema_from_path('schema.graphql')

query = ObjectType("Query")
query.set_field("listPosts", list_posts_resolver)
query.set_field("getPost", get_post_resolver)


@query.field("hello")
def resolve_hello(*_):
    return "Hello"


mutation = ObjectType("Mutation")
mutation.set_field("createPost", create_post_resolver)
mutation.set_field("updatePost", update_post_resolver)
mutation.set_field("deletePost", delete_post_resolver)

schema = make_executable_schema(
    type_defs, 
    query,
    mutation
)

explorer_html = ExplorerGraphiQL().html(None)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return explorer_html, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code