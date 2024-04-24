class Product:
    def __init__(self, price):
        # self.price = price
        self.set_price(price)

    def get_price(self):
        return self.price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price must be greater than zero")
        self.price = value


product = Product(-10)
print(product.price)
