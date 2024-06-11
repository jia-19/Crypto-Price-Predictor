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
        print("Message received: ", message)

        breakpoint()