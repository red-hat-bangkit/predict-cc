import uvicorn
from fastapi import FastAPI

import graphene
from starlette.graphql import GraphQLApp
from graphql.execution.executors.asyncio import AsyncioExecutor

from schemas import Query, Mutations

app = FastAPI()
app.add_route("/gql", GraphQLApp(schema=graphene.Schema(query=Query, mutation=Mutations), executor_class=AsyncioExecutor, graphiql=True))

def run(args):
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, headers=[("server", "bangkitws")])

if __name__ == "__main__":
    from settings.core import parser

    parser.set_defaults(func=run)

    args = parser.parse_args()
    args.func(args)