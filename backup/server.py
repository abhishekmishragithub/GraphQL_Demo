from flask import Flask
from graphene import ObjectType, String, Schema
from flask_graphql import GraphQLView

class Query(ObjectType):
    hello = String(description="Simple Hello")
    def resolve_hello(self, args, context, info):
        return "👋 Hey Pythonista's"

view_func = GraphQLView.as_view("graphql", schema=Schema(query=Query), graphiql=True)

app = Flask(__name__)
app.add_url_rule("/", view_func=view_func)

if __name__ == "__main__":
    app.run()