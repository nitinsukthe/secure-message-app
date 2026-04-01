import tkinter as tk
from tkinter import messagebox
from crypto_utils import encode_message, decode_message, save_to_file, load_from_file

def run_app():
    root = tk.Tk()
    root.title("🔐 Secure Message Encoder")
    root.geometry("520x450")
    root.config(bg="#1e1e1e")

    # Variables
    message_var = tk.StringVar()
    key_var = tk.StringVar()
    result_var = tk.StringVar()

    # Functions
    def encode():
        result = encode_message(message_var.get(), key_var.get())
        result_var.set(result)
        messagebox.showinfo("Success", "Message Encrypted")

    def decode():
        result = decode_message(message_var.get(), key_var.get())
        result_var.set(result)
        messagebox.showinfo("Success", "Message Decrypted")

    def save():
        save_to_file(result_var.get())
        messagebox.showinfo("Saved", "Encrypted message saved")

    def load():
        data = load_from_file()
        message_var.set(data)
        messagebox.showinfo("Loaded", "Message loaded")

    def copy():
        root.clipboard_clear()
        root.clipboard_append(result_var.get())
        messagebox.showinfo("Copied", "Copied to clipboard")

    def reset():
        message_var.set("")
        key_var.set("")
        result_var.set("")

    # UI Components
    label_style = {"bg": "#1e1e1e", "fg": "white", "font": ("Arial", 12)}

    tk.Label(root, text="Message", **label_style).pack(pady=5)
    tk.Entry(root, textvariable=message_var, width=50).pack()

    tk.Label(root, text="Secret Key", **label_style).pack(pady=5)
    tk.Entry(root, textvariable=key_var, show="*", width=50).pack()

    tk.Label(root, text="Result", **label_style).pack(pady=5)
    tk.Entry(root, textvariable=result_var, width=50).pack()

    # Buttons
    tk.Button(root, text="Encode", width=15, command=encode, bg="#4CAF50").pack(pady=5)
    tk.Button(root, text="Decode", width=15, command=decode, bg="#2196F3").pack(pady=5)

    tk.Button(root, text="Save", width=15, command=save).pack(pady=5)
    tk.Button(root, text="Load", width=15, command=load).pack(pady=5)

    tk.Button(root, text="Copy", width=15, command=copy, bg="#9C27B0", fg="white").pack(pady=5)
    tk.Button(root, text="Reset", width=15, command=reset, bg="#f44336", fg="white").pack(pady=5)

    root.mainloop()