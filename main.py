import tkinter as tk
from tkinter import ttk  # Pour Treeview
from Store import Store

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion de Stock du Magasin")
        
        self.store = Store()

        # Créer et placer vos widgets ici
        self.create_widgets()

    def create_widgets(self):
        # Créer un Treeview pour afficher les produits
        self.columns = ("ID", "Nom", "Description", "Prix", "Quantité", "Catégorie")
        self.product_table = ttk.Treeview(self.root, columns=self.columns, show='headings')
        
        # Définir les en-têtes pour les colonnes
        for col in self.columns:
            self.product_table.heading(col, text=col)
            self.product_table.column(col, width=100)  # Ajuster la largeur selon le contenu

        # Positionner le tableau dans la fenêtre
        self.product_table.pack(side="top", fill="both", expand=True)

        # Ajouter un bouton pour rafraîchir les données du tableau
        self.refresh_button = tk.Button(self.root, text="Rafraîchir les données", command=self.display_all_products)
        self.refresh_button.pack(side="bottom")

        # Afficher initialement tous les produits
        self.display_all_products()

    def display_all_products(self):
        # Supprimer les données existantes dans le tableau
        for item in self.product_table.get_children():
            self.product_table.delete(item)
        
        # Obtenir les produits et les afficher dans le tableau
        products = self.store.get_product()
        for product in products:
            category_name = self.store.get_category_name_by_id(product[5])
            # Ajouter les données du produit dans le tableau
            self.product_table.insert("", "end", values=(product[0], product[1], product[2], product[3], product[4], category_name))

# Création de la fenêtre et lancement de l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()