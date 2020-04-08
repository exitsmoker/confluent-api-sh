#!/usr/bin/python

import os
import sys
import requests

schema_registry_url = 'http://localhost:7001'
topic = 'avro-test2'
schema = '''
{
  "name": "avro-test2",
  "config": {
    "connector.class":"com.mongodb.kafka.connect.MongoSinkConnector",
    "tasks.max":"1",
    "topics":"avro-test2",
    "connection.uri":"mongodb://kafka:test@mongodb-service:2901",
    "database":"lucent",
    "collection":"avro-test2",
    "key.converter": "io.confluent.connect.avro.AvroConverter",
    "value.converter": "io.confluent.connect.avro.AvroConverter",
    "key.converter.schema.registry.url": "http://schema-registry-service:7002",
    "value.converter.schema.registry.url": "http://schema-registry-service:7002"
  }
}
'''

print("Schema Registry URL: " + schema_registry_url)
print("Topic: " + topic)
print()

payload = schema.replace("\"", "\\\"").replace("\t", "").replace("\n","")

url = schema_registry_url + "/connectors"
headers = {"Accept": "application/json", "Content-Type": "application/json"}

r = requests.post(url, headers=headers, data=schema)
if r.status_code == requests.codes.ok:
    print("Success")
else:
    r.raise_for_status()
