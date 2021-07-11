from flask import Flask, request
from graphene import ObjectType, String, Schema, Argument, Int
from flask_graphql import GraphQLView


class Query(ObjectType):
    hello = String(name = Argument(String, default_value="Stranger"),
    age = Argument(Int))


    def resolve_hello(self, args, context, info):
        return "👋 Hello your are {} old, welcome to PyCon India 2k19".format(args['name'], args['age'])

view_func = GraphQLView.as_view("graphql", schema=Schema(query=Query), graphiql=True)

app = Flask(__name__)
app.add_url_rule("/graphql", view_func=view_func)

if __name__ == "__main__":
    app.run()