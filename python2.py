import tkinter as tk
from tkinter import messagebox
import csv
import os

class InventoryApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Aplikasi Manajemen Inventaris")

        self.inventory = {}
        self.filename = 'inventory.csv'
        self.load_inventory()

        # Label dan Entry untuk nama barang
        self.label_item = tk.Label(root, text="Nama Barang:")
        self.label_item.grid(row=0, column=0)
        self.entry_item = tk.Entry(root)
        self.entry_item.grid(row=0, column=1)

        # Label dan Entry untuk jumlah barang
        self.label_quantity = tk.Label(root, text="Jumlah:")
        self.label_quantity.grid(row=1, column=0)
        self.entry_quantity = tk.Entry(root)
        self.entry_quantity.grid(row=1, column=1)

        # Tombol untuk menambah barang
        self.button_add = tk.Button(root, text="Tambah Barang", command=self.add_item)
        self.button_add.grid(row=2, column=0, columnspan=2)

        # Tombol untuk menghapus barang
        self.button_remove = tk.Button(root, text="Hapus Barang", command=self.remove_item)
        self.button_remove.grid(row=3, column=0, columnspan=2)

        # Tombol untuk menampilkan inventaris
        self.button_display = tk.Button(root, text="Tampilkan Inventaris", command=self.display_inventory)
        self.button_display.grid(row=4, column=0, columnspan=2)

        # Text area untuk menampilkan inventaris
        self.text_area = tk.Text(root, width=40, height=10)
        self.text_area.grid(row=5, column=0, columnspan=2)

    def load_inventory(self):
        """Load inventory from CSV file."""
        if os.path.exists(self.filename):
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    item, quantity = row
                    self.inventory[item] = int(quantity)

    def save_inventory(self):
        """Save inventory to CSV file."""
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for item, quantity in self.inventory.items():
                writer.writerow([item, quantity])

    def add_item(self):
        """Add item to inventory."""
        item = self.entry_item.get()
        quantity = self.entry_quantity.get()

        if item and quantity.isdigit():
            quantity = int(quantity)
            if item in self.inventory:
                self.inventory[item] += quantity
            else:
                self.inventory[item] = quantity
            self.save_inventory()
            messagebox.showinfo("Info", f"{quantity} {item}(s) ditambahkan ke inventaris.")
            self.entry_item.delete(0, tk.END)
            self.entry_quantity.delete(0, tk.END)
        else:
            messagebox.showwarning("Peringatan", "Nama barang tidak boleh kosong dan jumlah harus berupa angka.")

    def remove_item(self):
        """Remove item from inventory."""
        item = self.entry_item.get()
        quantity = self.entry_quantity.get()

        if item and quantity.isdigit():
            quantity = int(quantity)
            if item in self.inventory and self.inventory[item] >= quantity:
                self.inventory[item] -= quantity
                if self.inventory[item] == 0:
                    del self.inventory[item]
                self.save_inventory()
                messagebox.showinfo("Info", f"{quantity} {item}(s) dihapus dari inventaris.")
                self.entry_item.delete(0, tk.END)
                self.entry_quantity.delete(0, tk.END)
            else:
                messagebox.showwarning("Peringatan", "Barang tidak cukup atau tidak ada dalam inventaris.")
        else:
            messagebox.showwarning("Peringatan", "Nama barang tidak boleh kosong dan jumlah harus berupa angka.")

    def display_inventory(self):
        """Display current inventory."""
        self.text_area.delete(1.0, tk.END)  # Clear previous text
        if not self.inventory:
            self.text_area.insert(tk.END, "Inventaris kosong.")
        else:
            self.text_area.insert(tk.END, "Inventaris Saat Ini:\n")
            for item, quantity in self.inventory.items():
                self.text_area.insert(tk.END, f"{item}: {quantity}\n")

if _name_ == "_main_":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()