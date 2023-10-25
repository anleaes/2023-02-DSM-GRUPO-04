class Client:
    def __init__(
        self,
        *,
        first_name: str,
        last_name: str,
        address: str,
        cell_phone: str,
        email: str,
        gender: str,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.cell_phone = cell_phone
        self.email = email
        self.gender = gender