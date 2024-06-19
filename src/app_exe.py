import tkinter as tk
from tkinter import ttk
from translator import translate_text

class TranslationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Application de Traduction")
        self.geometry("400x300")

        # Ici je crée les boutons et widgets
        self.label = ttk.Label(self, text="Entrez le texte à traduire :")
        self.label.pack(pady=10)

        self.text_entry = ttk.Entry(self, width=40)
        self.text_entry.pack(pady=5)

        self.lang_label = ttk.Label(self, text="Choisissez la langue de destination :")
        self.lang_label.pack(pady=10)

        self.lang_var = tk.StringVar()
        self.lang_en = ttk.Radiobutton(self, text="Anglais", variable=self.lang_var, value="en")
        self.lang_es = ttk.Radiobutton(self, text="Espagnol", variable=self.lang_var, value="es")
        self.lang_zh = ttk.Radiobutton(self, text="Chinois", variable=self.lang_var, value="zh-cn")

        self.lang_en.pack(anchor=tk.W, padx=20)
        self.lang_es.pack(anchor=tk.W, padx=20)
        self.lang_zh.pack(anchor=tk.W, padx=20)

        self.translate_button = ttk.Button(self, text="Traduire", command=self.translate)
        self.translate_button.pack(pady=20)

        self.result_label = ttk.Label(self, text="")
        self.result_label.pack(pady=10)

    def translate(self):
        text = self.text_entry.get()
        dest_lang = self.lang_var.get()
        translated_text = translate_text(text, dest_lang)
        self.result_label.config(text=f"Texte traduit : {translated_text}")

if __name__ == "__main__":
    app = TranslationApp()
    app.mainloop()