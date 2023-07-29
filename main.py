import PyPDF2
import tkinter as tk
from tkinter import filedialog
def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        return text
def browse_files():
    file_path = filedialog.askopenfilename()
    if file_path:
        text = extract_text_from_pdf(file_path)
        text_box.delete('1.0', tk.END)
        text_box.insert(tk.END, text)
def on_click(event):
    browse_files()
root = tk.Tk()
root.title("PDF Reader")
browse_button = tk.Button(root, text="Browse")
browse_button.bind("<Button-1>", on_click)
browse_button.pack()
text_box = tk.Text(root, height=20, width=50)
text_box.pack()
root.mainloop()