import unittest
import json
from snapshottest import TestCase
from settings.settings import os
from graphene.test import Client
from graphene import Schema

from predict.gql.schemas import Query, Mutations


class TestCase(TestCase):
    snapshot_should_update = json.loads(os.environ.get('UPDATE_SNAPSHOT_TEST', "false").lower())

class TestGQLPredict(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        schema = Schema(query=Query, mutation=Mutations)
        cls.client = Client(schema)

    def test_query_hello_world(self):
        testcase = "{ helloWorld }"
        self.assertMatchSnapshot(self.client.execute(testcase))

    def test_query_bencana_in_city(self):
        testcase = '''{ bencanaInCity(city: "Jakarta", name:"banjir") {
                            name,
                            city {
                            name
                            },
                            predictions {
                            bencana
                            confidence
                            reason
                            }
                        }
                      }'''
        self.assertMatchSnapshot(self.client.execute(testcase))
    
    def test_query_bencana_in_location(self):
        testcase = '''{  bencanaInLocation(locationName: "Ciliwung", name:"banjir") {
                            name,
                            location {
                            name
                            latLong
                            },
                            prediction {
                            bencana
                            confidence
                            reason
                            }
                        }
                    }'''
        self.assertMatchSnapshot(self.client.execute(testcase))
    

if __name__ == "__main__":
    unittest.main()