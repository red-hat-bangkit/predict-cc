import graphene
from starlette.graphql import GraphQLApp
from graphql.execution.executors.asyncio import AsyncioExecutor

from .schemas import Query, Mutations

gql_app = GraphQLApp(schema=graphene.Schema(query=Query, mutation=Mutations), executor_class=AsyncioExecutor, graphiql=True)