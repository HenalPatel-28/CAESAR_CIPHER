import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

# Core Caesar Cipher Functions
def encrypt(text: str, shift: int) -> str:
    """
    Encrypts the given text using Caesar cipher with the specified shift.
    
    Args:
        text: The plaintext to encrypt
        shift: The number of positions to shift each character
        
    Returns:
        The encrypted ciphertext
    """
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text: str, shift: int) -> str:
    """
    Decrypts the given text using Caesar cipher with the specified shift.
    
    Args:
        text: The ciphertext to decrypt
        shift: The number of positions to shift each character back
        
    Returns:
        The decrypted plaintext
    """
    return encrypt(text, -shift)

def brute_force_decrypt(text: str) -> list:
    """
    Attempts all possible shifts (1-25) to decrypt the text.
    
    Args:
        text: The ciphertext to decrypt
        
    Returns:
        A list of all possible decrypted texts
    """
    possibilities = []
    for shift in range(1, 26):
        possibilities.append(decrypt(text, shift))
    return possibilities

class CaesarCipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Caesar Cipher Tool")
        self.root.geometry("600x500")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True)
        
        # Encrypt Tab
        self.encrypt_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.encrypt_tab, text='Encrypt')
        self.setup_encrypt_tab()
        
        # Decrypt Tab
        self.decrypt_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.decrypt_tab, text='Decrypt')
        self.setup_decrypt_tab()
        
        # Brute Force Tab
        self.brute_force_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.brute_force_tab, text='Brute Force')
        self.setup_brute_force_tab()
    
    def setup_encrypt_tab(self):
        # Input Label and Text
        ttk.Label(self.encrypt_tab, text="Plaintext:").pack(pady=(10, 0))
        self.plaintext_entry = tk.Text(self.encrypt_tab, height=5, width=60)
        self.plaintext_entry.pack(padx=10, pady=5)
        
        # Shift Value
        ttk.Label(self.encrypt_tab, text="Shift Value (0-25):").pack()
        self.shift_entry = ttk.Entry(self.encrypt_tab, width=5)
        self.shift_entry.pack()
        self.shift_entry.insert(0, " ")
        
        # Encrypt Button
        ttk.Button(self.encrypt_tab, text="Encrypt", command=self.perform_encryption).pack(pady=10)
        
        # Output Label and Text
        ttk.Label(self.encrypt_tab, text="Ciphertext:").pack()
        self.ciphertext_output = tk.Text(self.encrypt_tab, height=5, width=60, state='disabled')
        self.ciphertext_output.pack(padx=10, pady=5)
    
    def setup_decrypt_tab(self):
        # Input Label and Text
        ttk.Label(self.decrypt_tab, text="Ciphertext:").pack(pady=(10, 0))
        self.ciphertext_entry = tk.Text(self.decrypt_tab, height=5, width=60)
        self.ciphertext_entry.pack(padx=10, pady=5)
        
        # Shift Value
        ttk.Label(self.decrypt_tab, text="Shift Value (0-25):").pack()
        self.decrypt_shift_entry = ttk.Entry(self.decrypt_tab, width=5)
        self.decrypt_shift_entry.pack()
        self.decrypt_shift_entry.insert(0, " ")
        
        # Decrypt Button
        ttk.Button(self.decrypt_tab, text="Decrypt", command=self.perform_decryption).pack(pady=10)
        
        # Output Label and Text
        ttk.Label(self.decrypt_tab, text="Plaintext:").pack()
        self.plaintext_output = tk.Text(self.decrypt_tab, height=5, width=60, state='disabled')
        self.plaintext_output.pack(padx=10, pady=5)
    
    def setup_brute_force_tab(self):
        # Input Label and Text
        ttk.Label(self.brute_force_tab, text="Ciphertext:").pack(pady=(10, 0))
        self.brute_force_entry = tk.Text(self.brute_force_tab, height=5, width=60)
        self.brute_force_entry.pack(padx=10, pady=5)
        
        # Brute Force Button
        ttk.Button(self.brute_force_tab, text="Brute Force Decrypt", 
                  command=self.perform_brute_force).pack(pady=10)
        
        # Output Label and Text
        ttk.Label(self.brute_force_tab, text="All Possible Plaintexts:").pack()
        self.brute_force_output = scrolledtext.ScrolledText(
            self.brute_force_tab, height=15, width=60, wrap=tk.WORD)
        self.brute_force_output.pack(padx=10, pady=5)
        self.brute_force_output.config(state='disabled')
    
    def perform_encryption(self):
        try:
            plaintext = self.plaintext_entry.get("1.0", tk.END).strip()
            shift = int(self.shift_entry.get())
            
            if not plaintext:
                messagebox.showwarning("Warning", "Please enter some text to encrypt")
                return
            
            if shift < 0 or shift > 25:
                messagebox.showwarning("Warning", "Shift must be between 0 and 25")
                return
            
            ciphertext = encrypt(plaintext, shift)
            
            self.ciphertext_output.config(state='normal')
            self.ciphertext_output.delete("1.0", tk.END)
            self.ciphertext_output.insert("1.0", ciphertext)
            self.ciphertext_output.config(state='disabled')
        except ValueError:
            messagebox.showerror("Error", "Shift must be a number between 0 and 25")
    
    def perform_decryption(self):
        try:
            ciphertext = self.ciphertext_entry.get("1.0", tk.END).strip()
            shift = int(self.decrypt_shift_entry.get())
            
            if not ciphertext:
                messagebox.showwarning("Warning", "Please enter some text to decrypt")
                return
            
            if shift < 0 or shift > 25:
                messagebox.showwarning("Warning", "Shift must be between 0 and 25")
                return
            
            plaintext = decrypt(ciphertext, shift)
            
            self.plaintext_output.config(state='normal')
            self.plaintext_output.delete("1.0", tk.END)
            self.plaintext_output.insert("1.0", plaintext)
            self.plaintext_output.config(state='disabled')
        except ValueError:
            messagebox.showerror("Error", "Shift must be a number between 0 and 25")
    
    def perform_brute_force(self):
        ciphertext = self.brute_force_entry.get("1.0", tk.END).strip()
        
        if not ciphertext:
            messagebox.showwarning("Warning", "Please enter some text to decrypt")
            return
        
        possibilities = brute_force_decrypt(ciphertext)
        
        self.brute_force_output.config(state='normal')
        self.brute_force_output.delete("1.0", tk.END)
        
        for shift, text in enumerate(possibilities, 1):
            self.brute_force_output.insert(tk.END, f"Shift {shift:2}: {text}\n")
        
        self.brute_force_output.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = CaesarCipherApp(root)
    root.mainloop()