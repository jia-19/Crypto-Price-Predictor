from quixstreams import Application 
from src.kraken_api import KrakenWebSocketTradeAPI
from typing import List, Dict

def produce_trades(
        kafka_broker_address: str,
        kafka_topic: str,
) -> None:
    """
    Reads trades from Kraken Websocket API and saves them into 
    a Kafka topic.

    Args:
        kafka_broker_address (str): Address of Kafka broker
        kafka_topic (str): Name of Kafka topic

    Returns:
        None
    """
    app = Application(broker_address = kafka_broker_address)

    # topic to be used for saving trades
    topic = app.topic(name = kafka_topic, value_serializer = 'json')

    # Creating Kafka API Instance
    kraken_api = KrakenWebSocketTradeAPI(product_id='BTC/USD')


    #event = {"id": "1", "text": "Lorem ipsum dolor sit amet"}

    # Create a Producer instance
    with app.get_producer() as producer:

        while True:
            # Get trades from Kraken API
            trades: List[Dict] = kraken_api.get_trades()
            
            for trade in trades:
                # Serialize an event using the defined Topic 
                message = topic.serialize(key=trade["product_id"], 
                                          value=trade)

                # Produce a message into the Kafka topic
                producer.produce(
                    topic=topic.name, 
                    value=message.value, 
                    key=message.key
                )

                print("Message sent")
                
                
            from time import sleep
            sleep(1)


if __name__ == '__main__':
    produce_trades('localhost:19092', "trade")