kafka-avro-console-producer --broker-list localhost:9092 --topic mongoTest --property value.schema='{"type":"record", "name":"myrecord", "fields":[{"name":"f1","type":"string"}]}'
