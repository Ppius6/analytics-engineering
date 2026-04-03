class Product:
    inventory = []  # class-level variable: shared by ALL instances

    def __init__(self, product_id, name, category, quantity, price, supplier):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.supplier = supplier
        Product.inventory.append(self)

    @classmethod
    def add_product(cls, name, category, quantity, price, supplier):
        # Auto-generate an incremental product_id with no duplicates
        product_id = len(cls.inventory) + 1

        # Create a new Product object using the constructor
        new_product = cls(product_id, name, category, quantity, price, supplier)

        return "Product added successfully"

    @classmethod
    def update_product(cls, product_id, quantity=None, price=None, supplier=None):
        for product in cls.inventory:
            if product.product_id == product_id:
                # Only update fields that were actually passed in
                if quantity is not None:
                    product.quantity = quantity
                if price is not None:
                    product.price = price
                if supplier is not None:
                    product.supplier = supplier
                return "Product information updated successfully"
        return "Product not found"

    @classmethod
    def delete_product(cls, product_id):
        for product in cls.inventory:
            if product.product_id == product_id:
                cls.inventory.remove(product)
                return "Product deleted successfully"

        return "Product not found"


class Order:
    def __init__(self, order_id, products, customer_info=None):
        self.order_id = order_id
        self.products = products  # A list of (product_id, quantity) tuples
        self.customer_info = customer_info

    def place_order(self, product_id, quantity, customer_info=None):
        self.products.append((product_id, quantity))

        if customer_info is not None:
            self.customer_info = customer_info

        # Find the product in inventory and reduce its stock
        for product in Product.inventory:
            if product.product_id == product_id:
                product.quantity -= quantity

        return f"Order placed successfully. Order ID: {self.order_id}"


p1 = Product.add_product("Laptop", "Electronics", 50, 1000, "Supplier A")
print(p1)  # Product added successfully
print(Product.inventory[0].quantity)  # 50 — before order

update_p1 = Product.update_product(1, quantity=45, price=950)
print(update_p1)  # Product information updated successfully

order = Order(order_id=1, products=[])
order_placement = order.place_order(1, 2, customer_info="John Doe")
print(order_placement)  # Order placed successfully. Order ID: 1
print(Product.inventory[0].quantity)  # 48 — after order, correctly reduced

delete_p1 = Product.delete_product(1)
print(delete_p1)  # Product deleted successfully
