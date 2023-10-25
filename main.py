from models.category import Category
from models.client import Client
from models.client_socialnetwork import ClientSocialnetwork
from models.order import Order
from models.orderitem import OrderItem
from models.product import Product
from models.socialnetwork import Socialnetwork


def main():
  cliente_bruna = Client(
    first_name='Bruna',
    last_name='Borow Sky',
    address='Vila',
    cell_phone='9999999',
    email='borowSky@hotmail.com',
    gender='F'
  )

  rede_social = Socialnetwork(
    name='GraveDigger',
    description='Destruidores de competidores'
  )

  cliente_rede_social = ClientSocialnetwork(
    client=cliente_bruna,
    socialnetwork=rede_social
  )

  category_pas = Category(
    id=0,
    name='Pás',
    description='Pás de todos os tipos'
  )

  product_pa_coveiro = Product(
    name='Pá de coveiro',
    description='Uma pá assustadora',
    date_fabrication='1993-10-10',
    is_active=True,
    category=category_pas
  )

  ordem = Order(
    total_price=400,
    status='ACTIVE',
    client=cliente_bruna
  )

  ordem_item = OrderItem(
    quantity=4,
    unitary_price=100.0,
    order=ordem,
    product=product_pa_coveiro
  )

if __name__ == "__main__":
  main()
