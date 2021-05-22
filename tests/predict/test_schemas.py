import unittest
from graphene.test import Client
from graphene import Schema

from schemas import Query, Mutations

class TestGQLPredict(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        schema = Schema(query=Query, mutation=Mutations)
        cls.client = Client(schema)
    def test_query_helloWorld(self):
        testcase = "{ helloWorld }"
        expected = {'data': {'helloWorld': 'Hello World from FastAPI'}}
        self.assertDictEqual(self.client.execute(testcase), expected)
        

if __name__ == "__main__":
    unittest.main()