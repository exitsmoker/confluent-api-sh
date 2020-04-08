#!/usr/bin/python

import os
import sys
import requests

schema_registry_url = 'http://localhost:7002'
topic = 'avro-test2'
schema = '''
{"type": "record" ,"namespace": "orderbook" ,"name": "root" ,"fields": [{"name": "type" ,"type": "string"} ,{"name": "product_id" ,"type": "int"} ,{"name": "payload" ,"type": {"type": "array" ,"items": {"type": "map" ,"values": "long"}}}]}
'''

print("Schema Registry URL: " + schema_registry_url)
print("Topic: " + topic)
print()

payload = "{ \"schema\": \"" \
            + schema.replace("\"", "\\\"").replace("\t", "").replace("\n","") \
            + "\" }"

url = schema_registry_url + "/subjects/" + topic + "-value/versions"
headers = {"Accept": "application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json, application/json"}

r = requests.post(url, headers=headers, data=payload)
if r.status_code == requests.codes.ok:
    print("Success")
else:
    r.raise_for_status()
