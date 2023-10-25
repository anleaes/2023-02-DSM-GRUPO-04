from models.category import Category


class Product:
    def __init__(
        self,
        *,
        name: str,
        description: str,
        date_fabrication: str,
        is_active: bool,
        category: Category,
    ):
        self.name = name
        self.description = description
        self.date_fabrication = date_fabrication
        self.is_active = is_active
        self.category = category

    