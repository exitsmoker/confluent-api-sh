#!/usr/bin/python

import os
import sys
import requests

schema_registry_url = 'http://localhost:7003'
topic = 'avro-test2'
schema = '''
{
  "value_schema_id": 21,
  "records": [
    {
      "value":{"type":"seller","product_id":1,"payload":[{"1000":30}, {"1500":40}, {"2000":50}]}
    }
  ]
}
'''

print("Schema Registry URL: " + schema_registry_url)
print("Topic: " + topic)
print()

payload = schema.replace("\"", "\\\"").replace("\t", "").replace("\n","")

url = schema_registry_url + "/topics/" + topic
headers = {"Content-Type": "application/vnd.kafka.avro.v2+json", "Accept":"application/vnd.kafka.v2+json"}

r = requests.post(url, headers=headers, data=schema)
if r.status_code == requests.codes.ok:
    print("Success")
else:
    r.raise_for_status()
