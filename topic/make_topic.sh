kafka-topics --create --topic error --partitions 1 --replication-factor 3 \
  --if-not-exists --zookeeper localhost:2181 &&
kafka-topics --create --topic order --partitions 1 --replication-factor 3 \
  --if-not-exists --zookeeper localhost:2181 &&
kafka-topics --create --topic trade --partitions 1 --replication-factor 3 \
  --if-not-exists --zookeeper localhost:2181 &&
kafka-topics --create --topic canceled --partitions 1 --replication-factor 3 \
  --if-not-exists --zookeeper localhost:2181 &&
kafka-topics --create --topic match --partitions 1 --replication-factor 3 \
  --if-not-exists --zookeeper localhost:2181 &&
kafka-topics --create --topic vote --partitions 1 --replication-factor 3 \
  --if-not-exists --zookeeper localhost:2181 &&
kafka-topics --create --topic public_offering --partitions 1 --replication-factor 3 \
  --if-not-exists --zookeeper localhost:2181 &&
kafka-topics --create --topic product_news --partitions 1 --replication-factor 3 \
  --if-not-exists --zookeeper localhost:2181 &&
kafka-topics --create --topic orderbook_update --partitions 1 --replication-factor 3 \
  --if-not-exists --zookeeper localhost:2181
