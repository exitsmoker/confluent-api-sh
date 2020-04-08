const Kafka = require('node-rdkafka');
const producer = new Kafka.Producer({
  'metadata.broker.list': 'localhost:9092, localhost:19092, localhost:29092',
  'dr_cb': true
});
const registry = require('avro-schema-registry')('http://localhost:7002');

const schema = {"type": "record" ,"namespace": "orderbook" ,"name": "root" ,"fields": [{"name": "type" ,"type": "string"} ,{"name": "product_id" ,"type": "int"} ,{"name": "payload" ,"type": {"type": "array" ,"items": {"type": "map" ,"values": "long"}}}]}
const message = {"type":"seller","product_id":1,"payload":[{"1000":30}, {"1500":40}, {"2000":50}]};

registry.encodeMessageByTopicName('avro-test1', message)
  .then((msg) => {
    console.log('readyOn2');
    producer.connect();
    producer.on('ready', function() {
      console.log('readyOn3');
      try {
        producer.produce(
          'avro-test1',
          // optionally we can manually specify a partition for the message
          null,
          // Message to send. Must be a buffer
          msg,
          // for keyed messages, we also specify the key - note that this field is optional
          null,
          // you can send a timestamp here. If your broker version supports it,
          // it will get added. Otherwise, we default to 0
          Date.now(),
        );
      } catch (err) {
        console.error('A problem occurred when sending our message');
        console.error(err);
      }
    });
    producer.on('event', function() {
      console.error(arguments);
    })
    return registry.decode(msg);
  })
  .then((msg) => {
    console.log(msg);  // test message
    console.log(msg.product_id);
    console.log(msg.payload);
    console.log(msg.payload[1]);
  })
  .catch((err) => {
    console.log(err);
  });
