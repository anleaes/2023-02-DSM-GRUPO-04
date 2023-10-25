from models.client import Client


class Order:
    def __init__(
        self,
        *,
        total_price: float,
        status: str,
        client: Client
    ):
        self.total_price = total_price
        self.status = status
        self.client = client
        