import uvicorn
from fastapi import FastAPI

import graphene
from starlette.graphql import GraphQLApp
from graphql.execution.executors.asyncio import AsyncioExecutor

from schemas import Query, Mutations

app = FastAPI()

app.add_route("/gql", GraphQLApp(schema=graphene.Schema(query=Query, mutation=Mutations), executor_class=AsyncioExecutor, graphiql=True))

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, headers=[("server", "bangkitws")])