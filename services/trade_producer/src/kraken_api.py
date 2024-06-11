from typing import List, Dict
from websocket import create_connection
import json

class KrakenWebSocketTradeAPI:

    url = "wss://ws.kraken.com/v2"

    def __init__(self,
                 product_id: str):
        self.product_id = product_id
        self._ws = create_connection(self.url)
        
        print("Connection was established!")

        self._subscribe(product_id)


    def _subscribe(self, product_id: str):
        """"
            Establishes connection from local machine to Kraken API
            for the specified product_id

            in: Self
                product_id: string

            out: None
        """
        print(f"Subscribing to to trades for {product_id}")

        # Subscribing to Kraken's API
        msg = {
            
                "method": "subscribe",
                "params": {
                    "channel": "trade",
                    "symbol": [
                        product_id
                    ],
                    "snapshot": False
                }
        
        }

        self._ws.send(json.dumps(msg))

        print("Subscribed!")


        #Dumping first two messages as they are only confirmation of subscription
        _ = self._ws.recv()
        _ = self._ws.recv()

    def get_trades(self) -> List[Dict]:
        # mock_trades = [
        #     {
        #         'product_id': 'BTC-USD',
        #         'price': 60000,
        #         'volume': 0.01,
        #         'timestamp': 1630000000
        #     },
        #     {
        #         'product_ID': 'BTC-USD',
        #         'price': 55000,
        #         'volume': 0.01,
        #         'timestamp': 1630000500
        #     }
        # ]

        message = self._ws.recv()

        if 'heartbeat' in message:
            return []
        
        #Parsing string for trade information
        message = json.loads(message)

        trades = []

        #Extracting trade info from message received
        for trade in message["data"]:
            trades.append({
                'product_id': self.product_id ,
                'price': trade['price'],
                'volume' : trade['qty'],
                'timestamp' : trade['timestamp']
                })


        #print("Message received: ", message)

       # breakpoint()
        return trades