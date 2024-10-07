import tkinter as tk
from tkinter import messagebox

class AffineCipher:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.m = 27  # Size of the alphabet (A-Z + Space)
        self.inv_a = self.modular_inverse(a, self.m)
        
        if self.inv_a is None:
            raise ValueError("The key 'a' must be coprime with the modulus 27")

    def modular_inverse(self, a, m):
        """Find the modular inverse of 'a' under modulo 'm'."""
        for i in range(1, m):
            if (a * i) % m == 1:
                return i
        return None

    def char_to_index(self, char):
        """Convert character to numeric index."""
        if char == ' ':
            return 26
        else:
            return ord(char) - ord('A')

    def index_to_char(self, index):
        """Convert numeric index to character."""
        if index == 26:
            return ' '
        else:
            return chr(index + ord('A'))

    def encrypt(self, plaintext):
        """Encrypt the given plaintext using Affine cipher."""
        ciphertext = ""
        for char in plaintext:
            index = self.char_to_index(char)
            encrypted_index = (self.a * index + self.b) % self.m
            ciphertext += self.index_to_char(encrypted_index)
        return ciphertext

    def decrypt(self, ciphertext):
        """Decrypt the given ciphertext using Affine cipher."""
        plaintext = ""
        for char in ciphertext:
            index = self.char_to_index(char)
            decrypted_index = (self.inv_a * (index - self.b + self.m)) % self.m
            plaintext += self.index_to_char(decrypted_index)
        return plaintext

# GUI Code
class AffineCipherGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Affine Cipher")

        # Create and place labels and entry fields for input
        tk.Label(master, text="Plaintext/Ciphertext:").grid(row=0, column=0, padx=5, pady=5)
        self.input_text = tk.Entry(master, width=50)
        self.input_text.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(master, text="Key a:").grid(row=1, column=0, padx=5, pady=5)
        self.key_a = tk.Entry(master, width=10)
        self.key_a.grid(row=1, column=1, padx=5, pady=5, sticky='W')

        tk.Label(master, text="Key b:").grid(row=2, column=0, padx=5, pady=5)
        self.key_b = tk.Entry(master, width=10)
        self.key_b.grid(row=2, column=1, padx=5, pady=5, sticky='W')

        # Buttons for encryption and decryption
        encrypt_button = tk.Button(master, text="Encrypt", command=self.encrypt)
        encrypt_button.grid(row=3, column=0, padx=5, pady=5)

        decrypt_button = tk.Button(master, text="Decrypt", command=self.decrypt)
        decrypt_button.grid(row=3, column=1, padx=5, pady=5, sticky='W')

        # Output field
        tk.Label(master, text="Result:").grid(row=4, column=0, padx=5, pady=5)
        self.output_text = tk.Entry(master, width=50)
        self.output_text.grid(row=4, column=1, padx=5, pady=5)

    def encrypt(self):
        try:
            plaintext = self.input_text.get().upper()
            a = int(self.key_a.get())
            b = int(self.key_b.get())
            cipher = AffineCipher(a, b)
            ciphertext = cipher.encrypt(plaintext)
            self.output_text.delete(0, tk.END)
            self.output_text.insert(0, ciphertext)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def decrypt(self):
        try:
            ciphertext = self.input_text.get().upper()
            a = int(self.key_a.get())
            b = int(self.key_b.get())
            cipher = AffineCipher(a, b)
            plaintext = cipher.decrypt(ciphertext)
            self.output_text.delete(0, tk.END)
            self.output_text.insert(0, plaintext)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

if __name__ == '__main__':
    root = tk.Tk()
    gui = AffineCipherGUI(root)
    root.mainloop()