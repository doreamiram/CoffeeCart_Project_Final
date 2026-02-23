from Product import Product

class Coffee(Product):
    def __init__(self, product_id, name, price, milk_type="Regular"):
        super().__init__(product_id, name, price)
        self.milk_type = milk_type

    def get_price(self):
        """Polymorphism (סעיף 8 בנספח): מחיר משתנה לפי סוג החלב"""
        base_price = super().get_price()
        if self.milk_type in ["Oat", "Soy"]:
            return base_price + 3
        return base_price