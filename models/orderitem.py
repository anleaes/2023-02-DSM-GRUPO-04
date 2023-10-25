from models.order import Order
from models.product import Product


class OrderItem:
    def __init__(
        self,
        *,
        quantity: int,
        unitary_price: float,
        order: Order,
        product: Product
    ):
        self.quantity = quantity
        self.unitary_price = unitary_price
        self.order = order
        self.product = product