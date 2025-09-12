import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv

# ---------- initial sample data ----------
initial_data = [
    ("Sunil", 25),
    ("Pawan", 30),
    ("Ankur", 27),
    ("Ravi", 22),
    ("Priya", 29),
    ("Meena", 35),
    ("Arjun", 28),
    ("Kiran", 32),
    ("Sita", 24),
    ("Rahul", 26)
]

# ---------- window setup ----------
root = tk.Tk()
root.title("Treeview CRUD Example")
root.geometry("650x420")

# allow the tree to expand
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# ---------- Treeview (shows only headings -> hides '#0' column) ----------
columns = ("Name", "Age")
tree = ttk.Treeview(root, columns=columns, show="headings", selectmode="browse")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.column("Name", width=300, anchor="w")
tree.column("Age", width=80, anchor="center")

# scrollbar for tree
vsb = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=vsb.set)

tree.grid(row=0, column=0, sticky="nsew", padx=(10,0), pady=10)
vsb.grid(row=0, column=1, sticky="ns", pady=10, padx=(0,10))

# ---------- helper: populate initial data ----------
def populate_initial():
    for name, age in initial_data:
        tree.insert("", "end", values=(name, age))

populate_initial()

# ---------- form for Create / Update ----------
form = ttk.Frame(root)
form.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=(0,10))
form.columnconfigure(1, weight=1)

ttk.Label(form, text="Name").grid(row=0, column=0, sticky="w", padx=5, pady=4)
name_var = tk.StringVar()
name_entry = ttk.Entry(form, textvariable=name_var)
name_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=4)

ttk.Label(form, text="Age").grid(row=0, column=2, sticky="w", padx=5, pady=4)
age_var = tk.StringVar()
age_entry = ttk.Entry(form, textvariable=age_var, width=8)
age_entry.grid(row=0, column=3, sticky="w", padx=5, pady=4)

# ---------- CRUD functions ----------
def add_record():
    name = name_var.get().strip()
    age = age_var.get().strip()
    if not name:
        messagebox.showwarning("Validation", "Name cannot be empty.")
        return
    try:
        age_int = int(age)
        if age_int < 0:
            raise ValueError
    except ValueError:
        messagebox.showwarning("Validation", "Age must be a non-negative integer.")
        return

    # Insert into tree
    tree.insert("", "end", values=(name, age_int))
    clear_form()

def on_select(event):
    sel = tree.selection()
    if not sel:
        return
    item = sel[0]
    name, age = tree.item(item, "values")
    name_var.set(name)
    age_var.set(age)

def update_record():
    sel = tree.selection()
    if not sel:
        messagebox.showwarning("Selection", "Select a row to update.")
        return
    name = name_var.get().strip()
    age = age_var.get().strip()
    if not name:
        messagebox.showwarning("Validation", "Name cannot be empty.")
        return
    try:
        age_int = int(age)
        if age_int < 0:
            raise ValueError
    except ValueError:
        messagebox.showwarning("Validation", "Age must be a non-negative integer.")
        return

    item = sel[0]
    tree.item(item, values=(name, age_int))
    # Optional: keep selection on updated item
    tree.selection_set(item)
    tree.see(item)

def delete_record():
    sel = tree.selection()
    if not sel:
        messagebox.showwarning("Selection", "Select row(s) to delete.")
        return
    if not messagebox.askyesno("Confirm delete", "Delete the selected record(s)?"):
        return
    for item in sel:
        tree.delete(item)
    clear_form()

def clear_form():
    name_var.set("")
    age_var.set("")
    # remove selection
    try:
        tree.selection_remove(tree.selection())
    except Exception:
        pass

# ---------- Save / Load CSV ----------
def save_csv():
    path = filedialog.asksaveasfilename(defaultextension=".csv",
                                        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
    if not path:
        return
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age"])
        for item in tree.get_children():
            writer.writerow(tree.item(item, "values"))
    messagebox.showinfo("Saved", f"Data saved to:\n{path}")

def load_csv():
    path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
    if not path:
        return
    try:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            tree.delete(*tree.get_children())
            for row in reader:
                name = row.get("Name") or row.get("name") or row.get("NAME")
                age = row.get("Age") or row.get("age") or row.get("AGE")
                if name and age:
                    try:
                        age_int = int(age)
                    except ValueError:
                        age_int = age  # keep as-is
                    tree.insert("", "end", values=(name, age_int))
        messagebox.showinfo("Loaded", f"Data loaded from:\n{path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load CSV:\n{e}")

# ---------- buttons ----------
btn_frame = ttk.Frame(root)
btn_frame.grid(row=2, column=0, columnspan=2, pady=(0,10))

ttk.Button(btn_frame, text="Add", command=add_record).pack(side="left", padx=6)
ttk.Button(btn_frame, text="Update", command=update_record).pack(side="left", padx=6)
ttk.Button(btn_frame, text="Delete", command=delete_record).pack(side="left", padx=6)
ttk.Button(btn_frame, text="Clear", command=clear_form).pack(side="left", padx=6)

# Save/Load on the right
ttk.Button(btn_frame, text="Save CSV", command=save_csv).pack(side="right", padx=6)
ttk.Button(btn_frame, text="Load CSV", command=load_csv).pack(side="right", padx=6)

# ---------- bindings ----------
tree.bind("<<TreeviewSelect>>", on_select)
# double click quickly fills form so user can edit
tree.bind("<Double-1>", lambda e: on_select(e))

# focus name entry initially
name_entry.focus()

root.mainloop()
