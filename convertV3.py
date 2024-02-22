import pdfplumber
import pytesseract
from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog


def pdf_to_text(pdf_file, text_file):
    with pdfplumber.open(pdf_file) as pdf:
        text = ""
        for page in pdf.pages:
            if page.images:
                # Si la page contient des images, utiliser OCR pour extraire le texte
                for img in page.images:
                    img_obj = pdf.extract_image(img)
                    img_path = img_obj["stream"]
                    img = Image.open(img_path)
                    text += pytesseract.image_to_string(img)
            else:
                # Si la page ne contient pas d'image, extraire le texte normalement
                
                with pdfplumber.open(pdf_file) as pdf:
                    text = ""
                    for page in pdf.pages:
                        text += page.extract_text()
    
    with open(text_file, 'w', encoding='utf-8') as output_file:
        output_file.write(text)
    


def pdf_to_text(pdf_file, text_file):
    with pdfplumber.open(pdf_file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    
    with open(text_file, 'w', encoding='utf-8') as output_file:
        output_file.write(text)

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        input_directory_entry.delete(0, tk.END)
        input_directory_entry.insert(0, directory)

def convert_pdfs():
    input_directory = input_directory_entry.get()
    if input_directory:
        for filename in os.listdir(input_directory):
            if filename.endswith('.pdf'):
                pdf_path = os.path.join(input_directory, filename)
                text_path = os.path.splitext(pdf_path)[0] + '.txt'
                pdf_to_text(pdf_path, text_path)
        status_label.config(text="Conversion terminée !")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Convertir des fichiers PDF en texte")

# Cadre pour le champ d'entrée et le bouton
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Champ d'entrée pour le répertoire
input_directory_label = tk.Label(input_frame, text="Répertoire d'entrée:")
input_directory_label.grid(row=0, column=0)

input_directory_entry = tk.Entry(input_frame, width=50)
input_directory_entry.grid(row=0, column=1)

browse_button = tk.Button(input_frame, text="Parcourir", command=select_directory)
browse_button.grid(row=0, column=2)

# Bouton pour démarrer la conversion
convert_button = tk.Button(root, text="Convertir en texte", command=convert_pdfs)
convert_button.pack(pady=10)

# Étiquette pour afficher le statut
status_label = tk.Label(root, text="")
status_label.pack()

# Lancer la boucle principale de l'interface graphique
root.mainloop()
