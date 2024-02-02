from Product import Product
from Category import Category  

class Store:
    def __init__(self):
        self.product_instance = Product()
        self.category_instance = Category()

    # Méthodes liées aux produits
    def add_product(self, name, description, price, quantity, id_category):
        self.product_instance.add_product(name, description, price, quantity, id_category)

    def get_product(self):
        return self.product_instance.get_product()

    def get_product_by_id(self, id):
        return self.product_instance.get_product_by_id(id)
    
    def update_product(self, id, name, description, price, quantity, id_category):
        self.product_instance.update_product(id, name, description, price, quantity, id_category)

    def delete_product(self, id):
        self.product_instance.delete_product(id)

    def get_products_by_category(self, id_category):
        return self.product_instance.get_product_by_category(id_category)

    def get_category_name_by_id(self, id_category):
        category = self.category_instance.get_category_by_id(id_category)
        if category:
            return category[1]  # Supposons que la colonne 1 contient le nom de la catégorie
        else:
            return "Catégorie inconnue"

    def display_products_with_categories(self):
        products = self.product_instance.get_product()  # Obtenir tous les produits
        for product in products:
            category_name = self.get_category_name_by_id(product[5])  # Obtenir le nom de la catégorie
            print(f"Catégorie: {category_name}")


    # Méthodes liées aux catégories
    def add_category(self, name):
        self.category_instance.add_category(name)

    def get_category(self):
        return self.category_instance.get_categories()

    def get_category_by_id(self, id):
        return self.category_instance.get_category_by_id(id)

    def update_category(self, id, name):
        self.category_instance.update_category(id, name)

    def delete_category(self, id):
        self.category_instance.delete_category(id)