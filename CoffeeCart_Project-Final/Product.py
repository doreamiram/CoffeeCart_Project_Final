class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.__price = price  # Encapsulation (סעיף 6 בנספח)

    def get_price(self):
        """שימוש ב-Getter המאפשר פולימורפיזם בעתיד"""
        return self.__price

    def __repr__(self):
        """Operator Overloading (סעיף 11 בנספח)"""
        return f"{self.name} (₪{self.get_price()})"