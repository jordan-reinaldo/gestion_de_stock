import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import csv
from Store import Store
from tkinter import filedialog

class Main:
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
            self.product_table.column(col, width=120)  # Ajuster la largeur selon le contenu

        # Positionner le tableau dans la fenêtre
        self.product_table.pack(side="top", fill="both", expand=True)

        # Bouton pour ajouter un produit
        self.add_product_button = tk.Button(self.root, text="Ajouter un produit", command=self.add_product)
        self.add_product_button.pack(side="left")

        # Bouton pour supprimer un produit
        self.delete_product_button = tk.Button(self.root, text="Supprimer un produit", command=self.delete_product)
        self.delete_product_button.pack(side="left")

        # Bouton pour modifier un produit
        self.update_product_button = tk.Button(self.root, text="Modifier un produit", command=self.update_product)
        self.update_product_button.pack(side="left")

        self.export_button = tk.Button(self.root, text="Exporter vers CSV", command=self.export_to_csv)
        self.export_button.pack(side="left")


        # Afficher initialement tous les produits
        self.display_all_products()

    def add_product(self):
        # Ici, demandez les détails du produit à l'utilisateur, par exemple avec simpledialog ou un formulaire personnalisé
        name = simpledialog.askstring("Nom", "Entrez le nom du produit:")
        description = simpledialog.askstring("Description", "Entrez la description du produit:")
        price = simpledialog.askfloat("Prix", "Entrez le prix du produit:")
        quantity = simpledialog.askinteger("Quantité", "Entrez la quantité du produit:")
        category_id = simpledialog.askinteger("Catégorie", "Entrez le numéro de catégorie du produit:")
        
        # Vous n'avez pas besoin de convertir le nom de la catégorie en ID, car vous utilisez l'ID directement
        
        if name and description and price is not None and quantity is not None and category_id is not None:
            self.store.add_product(name, description, price, quantity, category_id)
            self.display_all_products()  # Rafraîchir la liste des produits
        else:
            messagebox.showerror("Erreur", "Informations sur le produit manquantes ou incorrectes.")

    def delete_product(self):
        selected_item = self.product_table.focus()  # Obtenir l'élément sélectionné
        if not selected_item:
            messagebox.showwarning("Attention", "Veuillez sélectionner un produit à supprimer.")
            return
        
        product_id = self.product_table.item(selected_item)['values'][0]
        self.store.delete_product(product_id)
        self.display_all_products()  # Rafraîchir la liste des produits

    def update_product(self):
        selected_item = self.product_table.focus()  # Obtenir l'élément sélectionné
        if not selected_item:
            messagebox.showwarning("Attention", "Veuillez sélectionner un produit à modifier.")
            return
        
        product_id = self.product_table.item(selected_item)['values'][0]

        # Vous pouvez demander les nouvelles informations du produit ici
        new_name = simpledialog.askstring("Nom", "Entrez le nouveau nom du produit:", initialvalue="Nom actuel")
        new_description = simpledialog.askstring("Description", "Entrez la nouvelle description du produit:", initialvalue="Description actuelle")
        new_price = simpledialog.askfloat("Prix", "Entrez le nouveau prix du produit:", initialvalue=0.0)
        new_quantity = simpledialog.askinteger("Quantité", "Entrez la nouvelle quantité du produit:", initialvalue=0)
        new_category_id = simpledialog.askinteger("Catégorie", "Entrez le nouvel ID de catégorie du produit:", initialvalue=0)
        # Vérifier que toutes les informations ont été fournies
        if new_name and new_description and new_price is not None and new_quantity is not None and new_category_id is not None:
            # Mise à jour du produit
            self.store.update_product(product_id, new_name, new_description, new_price, new_quantity, new_category_id)
            self.display_all_products()  # Rafraîchir la liste des produits
        else:
            messagebox.showerror("Erreur", "Informations sur le produit manquantes ou incorrectes.")


    def display_all_products(self):
        # Supprimer les données existantes dans le tableau
        for item in self.product_table.get_children():
            self.product_table.delete(item)
        
        # Obtenir les produits et les afficher dans le tableau
        products = self.store.get_product()
        for product in products:
            category_id = product[5]  # Obtenez directement l'ID de la catégorie depuis les données du produit
            category_name = self.store.get_category_by_id(category_id)  # Obtenez le nom de la catégorie à partir de l'ID
            self.product_table.insert("", "end", values=(product[0], product[1], product[2], product[3], product[4], category_name))

    def export_to_csv(self):
        # Obtenir les produits avec les noms des catégories
        products_with_categories = self.store.get_products_with_categories()
        
        # Demander à l'utilisateur où enregistrer le fichier CSV
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Fichiers CSV", "*.csv")])
        if not file_path:
            return  # L'utilisateur a annulé l'enregistrement

        try:
            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                # Écrire les en-têtes
                writer.writerow(["ID", "Nom", "Description", "Prix", "Quantité", "Catégorie"])

                # Écrire les données
                for product in products_with_categories:
                    # Assurez-vous que l'indice pour le nom de la catégorie est correct
                    writer.writerow([product[0], product[1], product[2], product[3], product[4], product[-1]])  # Utilisez product[-1] si le nom de la catégorie est le dernier élément

            messagebox.showinfo("Export CSV", "Les données ont été exportées avec succès vers le fichier CSV.")
        except Exception as e:
            messagebox.showerror("Erreur d'exportation", f"Une erreur s'est produite lors de l'exportation des données : {str(e)}")

# Création de la fenêtre et lancement de l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.mainloop()