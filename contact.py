import tkinter as tk
from tkinter import messagebox

# Sample data structure to store contacts
contacts = []


def add_contact():
    name = entry_name.get()
    phone_number = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    contacts.append({
        'Name': name,
        'Phone': phone_number,
        'Email': email,
        'Address': address
    })

    messagebox.showinfo('Contact Added', 'Contact has been added successfully.')
    clear_fields()
    view_contact_list()


def view_contact_list():
    contact_list.delete(0, tk.END)  # Clear existing list

    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['Name']}: {contact['Phone']}")


def search_contact():
    search_term = entry_search.get().lower()
    search_results.delete(0, tk.END)  # Clear existing results

    for contact in contacts:
        if search_term in contact['Name'].lower() or search_term in contact['Phone']:
            search_results.insert(tk.END, f"{contact['Name']}: {contact['Phone']}")


def clear_fields():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)


# Create the main application window
root = tk.Tk()
root.title("Contact Management App")
root.configure(bg='lightblue')

# Create and place widgets
tk.Label(root, text="Name:", bg='lightblue').grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Phone Number:", bg='lightblue').grid(row=1, column=0)
entry_phone = tk.Entry(root)
entry_phone.grid(row=1, column=1)

tk.Label(root, text="Email:", bg='lightblue').grid(row=2, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1)

tk.Label(root, text="Address:", bg='lightblue').grid(row=3, column=0)
entry_address = tk.Entry(root)
entry_address.grid(row=3, column=1)

add_button = tk.Button(root, text="Add Contact", command=add_contact, bg='green', fg='white')
add_button.grid(row=4, column=0, columnspan=2, pady=10)

view_button = tk.Button(root, text="View Contact List", command=view_contact_list, bg='blue', fg='white')
view_button.grid(row=5, column=0, columnspan=2, pady=10)

tk.Label(root, text="Search:", bg='lightblue').grid(row=6, column=0)
entry_search = tk.Entry(root)
entry_search.grid(row=6, column=1)
search_button = tk.Button(root, text="Search Contact", command=search_contact, bg='purple', fg='white')
search_button.grid(row=7, column=0, columnspan=2, pady=10)

contact_list = tk.Listbox(root, bg='white')
contact_list.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

search_results = tk.Listbox(root, bg='white')
search_results.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
