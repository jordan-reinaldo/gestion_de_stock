from Db import DB

class Category:
    def __init__(self):
        self.db = DB()

    def add_category(self, name):
        query = "INSERT INTO category (name) VALUES (%s)"
        self.db.execute(query, (name,))

    def get_categories(self):
        query = "SELECT * FROM category"
        self.db.execute(query)
        return self.db.fetchall()
    
    def get_category_by_id(self, id):
        query = "SELECT * FROM category WHERE id = %s"
        self.db.execute(query, (id,))
        return self.db.fetchone()
    
    def update_category(self, id, name):
        query = "UPDATE category SET name = %s WHERE id = %s"
        self.db.execute(query, (name, id))

    def delete_category(self, id):
        query = "DELETE FROM category WHERE id = %s"
        self.db.execute(query, (id,))

    def get_category_by_name(self, name):
        query = "SELECT id FROM category WHERE name = %s"
        self.db.execute(query, (name,))
        result = self.db.fetchone()
        if result:
            return result[0]
        else:
            return None
