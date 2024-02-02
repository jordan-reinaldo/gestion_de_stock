from Db import DB

class Product:
    def __init__(self):
        self.db = DB()

    def add_product(self, name, description, price, quantity, id_category):
        query = "INSERT INTO product (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)"
        self.db.execute(query, (name, description, price, quantity, id_category))

    def get_product(self):
        query = "SELECT * FROM product"
        self.db.execute(query)
        return self.db.fetchall()

    def get_product_by_id(self, id):
        query = "SELECT * FROM product WHERE id = %s"
        self.db.execute(query, (id,))
        return self.db.fetchone()
    
    def update_product(self, id, name, description, price, quantity, id_category):
        query = "UPDATE product SET name = %s, description = %s, price = %s, quantity = %s, id_category = %s WHERE id = %s"
        self.db.execute(query, (name, description, price, quantity, id_category, id))
   
    def delete_product(self, id):
        query = "DELETE FROM product WHERE id = %s"
        self.db.execute(query, (id,))
    
    def get_product_by_category(self, id_category):
        query = "SELECT * FROM product WHERE id_category = %s"
        self.db.execute(query, (id_category,))
        return self.db.fetchall()
    
    def get_products_with_categories(self):
        query = """
        SELECT product.*, category.name AS category_name
        FROM product
        JOIN category ON product.id_category = category.id
        """
        self.db.execute(query)
        return self.db.fetchall()