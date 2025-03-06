import tkinter as tk
from tkinter import messagebox, filedialog
import json
from faker import Faker

fake = Faker()

class FakeDataGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Fake Data Generator")
        self.root.geometry("400x400")
        
        self.style_var = tk.StringVar(value="Tech Blue")
        
        self.create_widgets()
        self.apply_theme()
    
    def create_widgets(self):
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.pack()
        self.name_text = tk.Entry(self.root, width=40)
        self.name_text.pack()
        
        self.email_label = tk.Label(self.root, text="Email:")
        self.email_label.pack()
        self.email_text = tk.Entry(self.root, width=40)
        self.email_text.pack()
        
        self.address_label = tk.Label(self.root, text="Address:")
        self.address_label.pack()
        self.address_text = tk.Entry(self.root, width=40)
        self.address_text.pack()
        
        self.generate_button = tk.Button(self.root, text="Generate", command=self.generate_data)
        self.generate_button.pack()
        
        self.copy_button = tk.Button(self.root, text="Copy to Clipboard", command=self.copy_data)
        self.copy_button.pack()
        
        self.surprise_button = tk.Button(self.root, text="Surprise Me!", command=self.surprise_me)
        self.surprise_button.pack()
        
        self.save_button = tk.Button(self.root, text="Export to JSON", command=self.export_json)
        self.save_button.pack()
        
        self.theme_menu = tk.OptionMenu(self.root, self.style_var, "Tech Blue", "Paper Theme", command=self.apply_theme)
        self.theme_menu.pack()
    
    def generate_data(self):
        name = fake.name()
        email = fake.email()
        address = fake.address()
        
        self.name_text.delete(0, tk.END)
        self.name_text.insert(0, name)
        
        self.email_text.delete(0, tk.END)
        self.email_text.insert(0, email)
        
        self.address_text.delete(0, tk.END)
        self.address_text.insert(0, address)
    
    def copy_data(self):
        data = f"Name: {self.name_text.get()}\nEmail: {self.email_text.get()}\nAddress: {self.address_text.get()}"
        self.root.clipboard_clear()
        self.root.clipboard_append(data)
        self.root.update()
        messagebox.showinfo("Copied", "Data copied to clipboard!")
    
    def surprise_me(self):
        self.generate_data()
    
    def export_json(self):
        data = {
            "name": self.name_text.get(),
            "email": self.email_text.get(),
            "address": self.address_text.get()
        }
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'w') as json_file:
                json.dump(data, json_file, indent=4)
            messagebox.showinfo("Saved", "Data exported successfully!")
    
    def apply_theme(self, *args):
        theme = self.style_var.get()
        if theme == "Tech Blue":
            self.root.configure(bg="#001f3f")
            color, text_color = "#001f3f", "white"
        else:
            self.root.configure(bg="#f5f5dc")
            color, text_color = "#f5f5dc", "black"
        
        for widget in self.root.winfo_children():
            if isinstance(widget, (tk.Label, tk.Entry, tk.Button)):
                widget.configure(bg=color, fg=text_color)

if __name__ == "__main__":
    root = tk.Tk()
    app = FakeDataGenerator(root)
    root.mainloop()