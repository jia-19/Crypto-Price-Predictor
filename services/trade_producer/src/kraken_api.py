from typing import List, Dict

class KrakenWebSocketTradeAPI:

    def __init__(self):
        pass


    def get_trades(self) -> List[Dict]:
        mock_trades = [
            {
                'product_ID': 'BTC-USD',
                'price': 60000,
                'volume': 0.01,
                'timestamp': 1630000000
            },
            {
                'product_ID': 'BTC-USD',
                'price': 55000,
                'volume': 0.01,
                'timestamp': 1630000500
            }
        ]

        return mock_trades