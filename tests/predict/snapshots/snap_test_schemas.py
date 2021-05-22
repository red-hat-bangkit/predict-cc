# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGQLPredict::test_query_bencana_in_city 1'] = {
    'data': {
        'bencanaInCity': {
            'city': {
                'name': 'Jakarta'
            },
            'name': 'banjir',
            'predictions': [
                {
                    'bencana': 'banjir',
                    'confidence': 0.85,
                    'reason': 'Curah Hujan'
                },
                {
                    'bencana': 'banjir',
                    'confidence': 0.75,
                    'reason': 'Luapan Sungai'
                }
            ]
        }
    }
}

snapshots['TestGQLPredict::test_query_bencana_in_location 1'] = {
    'data': {
        'bencanaInLocation': {
            'location': {
                'latLong': '12345, 53421',
                'name': 'Ciliwung'
            },
            'name': 'banjir',
            'prediction': {
                'bencana': 'banjir',
                'confidence': 0.85,
                'reason': 'Curah Hujan'
            }
        }
    }
}

snapshots['TestGQLPredict::test_query_helloWorld 1'] = {
    'data': {
        'helloWorld': 'Hello World from FastAPI'
    }
}

snapshots['TestGQLPredict::test_query_hello_world 1'] = {
    'data': {
        'helloWorld': 'Hello World from FastAPI'
    }
}
