import tkinter as tk
from tkinter import messagebox, simpledialog, Entry, Label

# Global variables
users = [["admin", "password"]]  # Sample user for demonstration

# Authentication functions

# Function to handle user login
def login():
    username = simpledialog.askstring("Login", "Enter Username:")
    password = simpledialog.askstring("Login", "Enter Password:", show="*")
    
    if [username, password] in users:
        messagebox.showinfo("Login", "Login Successful!")
    else:
        messagebox.showerror("Login", "Invalid Username or Password!")

# Function to handle user registration
def add_user():
    username = simpledialog.askstring("Register", "Choose a Username:")
    password = simpledialog.askstring("Register", "Choose a Password:", show="*")
    
    if any(user[0] == username for user in users):
        messagebox.showerror("Register", "Username already exists!")
    else:
        users.append([username, password])
        messagebox.showinfo("Register", "User Registered Successfully!")

# Classes functionality

# Function to display the window for adding a new class
def classes_functionality():
    class_window = tk.Toplevel()
    class_window.title("Add Class")

    Label(class_window, text="Class Code:").grid(row=0, column=0)
    class_code_entry = Entry(class_window)
    class_code_entry.grid(row=0, column=1)

    Label(class_window, text="Class Name:").grid(row=1, column=0)
    class_name_entry = Entry(class_window)
    class_name_entry.grid(row=1, column=1)

    Label(class_window, text="Start Date (dd/mm/yy):").grid(row=2, column=0)
    start_date_entry = Entry(class_window)
    start_date_entry.grid(row=2, column=1)

    Label(class_window, text="Description:").grid(row=3, column=0)
    description_entry = Entry(class_window)
    description_entry.grid(row=3, column=1)

    Label(class_window, text="Number of Sessions:").grid(row=4, column=0)
    sessions_entry = Entry(class_window)
    sessions_entry.grid(row=4, column=1)

    # Wrapper function to capture the entries and pass them to save_class
    def save_class_wrapper():
        save_class(class_code_entry.get(), class_name_entry.get(), start_date_entry.get(), description_entry.get(), sessions_entry.get())

    tk.Button(class_window, text="Save", command=save_class_wrapper).grid(row=5, column=0)
    tk.Button(class_window, text="Back", command=class_window.destroy).grid(row=5, column=1)

# Function to save the class details to a file
def save_class(code, name, date, description, sessions):
    # Simple date validation
    date_parts = date.split("/")
    if len(date_parts) != 3 or len(date_parts[0]) != 2 or len(date_parts[1]) != 2 or len(date_parts[2]) != 2:
        messagebox.showerror("Error", "Invalid date format!")
        return

    if not sessions.isdigit():
        messagebox.showerror("Error", "Number of sessions must be an integer!")
        return

    with open("ArtClassDetails.txt", "a") as file:
        file.write(code + "," + name + "," + date + "," + description + "," + sessions + "\n")

    messagebox.showinfo("Success", "Class details saved successfully!")

# Payroll functionality

# Function to display the payroll window
def payroll_functionality():
    payroll_window = tk.Toplevel()
    payroll_window.title("Payroll")

    Label(payroll_window, text="Gross Pay:").grid(row=0, column=0)
    gross_pay_entry = Entry(payroll_window)
    gross_pay_entry.grid(row=0, column=1)

    Label(payroll_window, text="Tax:").grid(row=2, column=0)
    tax_label = Label(payroll_window, text="")
    tax_label.grid(row=2, column=1)

    Label(payroll_window, text="National Insurance:").grid(row=3, column=0)
    ni_label = Label(payroll_window, text="")
    ni_label.grid(row=3, column=1)

    Label(payroll_window, text="Pension Contribution:").grid(row=4, column=0)
    pension_label = Label(payroll_window, text="")
    pension_label.grid(row=4, column=1)

    Label(payroll_window, text="Deductions:").grid(row=5, column=0)
    deductions_label = Label(payroll_window, text="")
    deductions_label.grid(row=5, column=1)

    Label(payroll_window, text="Net Pay:").grid(row=6, column=0)
    net_pay_label = Label(payroll_window, text="")
    net_pay_label.grid(row=6, column=1)

    # Wrapper function to capture the gross pay entry and pass it to calculate_payroll
    def calculate_payroll_wrapper():
        calculate_payroll(gross_pay_entry, tax_label, ni_label, pension_label, deductions_label, net_pay_label)

    tk.Button(payroll_window, text="Calculate", command=calculate_payroll_wrapper).grid(row=1, column=0, columnspan=2)
    tk.Button(payroll_window, text="Back", command=payroll_window.destroy).grid(row=7, column=0, columnspan=2)

    # Function to calculate and display the payroll details
    def calculate_payroll(entry, tax_lbl, ni_lbl, pension_lbl, deductions_lbl, net_lbl):
        gross_pay = float(entry.get())
        if gross_pay <= 0:
            messagebox.showerror("Error", "Gross Pay must be greater than 0!")
            return

        tax = 0.19 * gross_pay
        national_insurance = 0.125 * gross_pay
        pension_contribution = 0.10 * gross_pay
        deductions = tax + national_insurance + pension_contribution
        net_pay = gross_pay - deductions

        tax_lbl.config(text=str(tax))
        ni_lbl.config(text=str(national_insurance))
        pension_lbl.config(text=str(pension_contribution))
        deductions_lbl.config(text=str(deductions))
        net_lbl.config(text=str(net_pay))

# Main GUI

# Function to display the main menu
def main_menu():
    root = tk.Tk()
    root.title("Parkwood Vale Arts Club System")
    
    tk.Label(root, text="Main Menu", font=("Arial", 16)).pack(pady=20)
    
    tk.Button(root, text="Login", command=login).pack(pady=10)
    tk.Button(root, text="Register", command=add_user).pack(pady=10)
    tk.Button(root, text="Classes", command=classes_functionality).pack(pady=10)
    tk.Button(root, text="Payroll", command=payroll_functionality).pack(pady=10)
    tk.Button(root, text="Exit", command=root.quit).pack(pady=10)
    
    root.mainloop()

# Run the main menu
main_menu()
