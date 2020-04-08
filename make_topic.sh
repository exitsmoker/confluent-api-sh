kafka-topics --create --topic avro-test2 --partitions 1 --replication-factor 3 \
  --if-not-exists --zookeeper localhost:2181 
