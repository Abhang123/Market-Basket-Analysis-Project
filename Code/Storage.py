import tkinter as tk
from tkinter import filedialog
import databaseObject
import csv
db = databaseObject.dbObj()
# Function to convert CSV to a list of dictionaries
def app():
    def csv_to_dict_list(csv_file):
        dict_list = []
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                dict_list.append(row)
        return dict_list

    # Function to upload data to Firestore
    def upload_to_firestore(collection_name, data):
        collection_ref = db.collection(collection_name)
        for item in data:
            collection_ref.add(item)

    # Function to handle file selection
    def select_file():
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            file_path_entry.delete(0, tk.END)
            file_path_entry.insert(0, file_path)

    # Function to upload CSV to Firestore
    def upload_csv():
        file_path = file_path_entry.get()
        collection_name = collection_name_entry.get()
        if not collection_name:
            status_label.config(text="Please enter a collection name", fg="red")
            return

        try:
            data_from_csv = csv_to_dict_list(file_path)
            upload_to_firestore(collection_name, data_from_csv)
            status_label.config(text="CSV data uploaded to Firestore successfully", fg="green")
        except Exception as e:
            status_label.config(text=f"Error: {e}", fg="red")

    # Create main window
    root = tk.Tk()
    root.title("CSV to Firestore Uploader")

    # Create form frame
    form_frame = tk.Frame(root)
    form_frame.pack(padx=10, pady=10)

    # Create form components
    collection_name_label = tk.Label(form_frame, text="Firestore Collection Name:")
    collection_name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    collection_name_entry = tk.Entry(form_frame)
    collection_name_entry.grid(row=0, column=1, padx=5, pady=5)

    file_path_label = tk.Label(form_frame, text="CSV File Path:")
    file_path_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    file_path_entry = tk.Entry(form_frame)
    file_path_entry.grid(row=1, column=1, padx=5, pady=5)

    select_button = tk.Button(form_frame, text="Select File", command=select_file)
    select_button.grid(row=1, column=2, padx=5, pady=5)

    upload_button = tk.Button(form_frame, text="Upload", command=upload_csv)
    upload_button.grid(row=2, column=1, padx=5, pady=5)

    status_label = tk.Label(root, text="", fg="green")
    status_label.pack(pady=5)

    # Run the main event loop
    root.mainloop()

        


