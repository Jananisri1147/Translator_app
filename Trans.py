import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# Get supported languages
translator = GoogleTranslator(source='auto', target='english')
languages_dict = translator.get_supported_languages(as_dict=True)
lang_names = list(languages_dict.keys())

# Add 'auto' as a language option for source language
src_lang_display = ['auto'] + lang_names
languages_dict['auto'] = 'auto'

# GUI setup
root = tk.Tk()
root.title("Google Translate GUI")
root.geometry("750x500")
root.config(bg="#f2f2f2")
root.resizable(False, False)

# Functions
def translate_text():
    src_lang_key = src_lang_var.get()
    tgt_lang_key = tgt_lang_var.get()
    text = input_text.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Empty Input", "Please enter some text.")
        return

    try:
        src_code = languages_dict[src_lang_key]
        tgt_code = languages_dict[tgt_lang_key]

        translated = GoogleTranslator(source=src_code, target=tgt_code).translate(text)
        output_text.config(state='normal')
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)
        output_text.config(state='disabled')
    except Exception as e:
        messagebox.showerror("Translation Failed", str(e))

def copy_to_clipboard():
    root.clipboard_clear()
    output_text.config(state='normal')
    translated_text = output_text.get("1.0", tk.END).strip()
    output_text.config(state='disabled')
    root.clipboard_append(translated_text)
    messagebox.showinfo("Copied", "Translated text copied to clipboard.")

def clear_all():
    input_text.delete("1.0", tk.END)
    output_text.config(state='normal')
    output_text.delete("1.0", tk.END)
    output_text.config(state='disabled')

# Language selection
src_lang_var = tk.StringVar(value="auto")
tgt_lang_var = tk.StringVar(value="english")

font_style = ("Segoe UI", 10)

tk.Label(root, text="From Language:", bg="#f2f2f2", font=font_style).place(x=40, y=20)
src_menu = ttk.Combobox(root, textvariable=src_lang_var, values=src_lang_display, width=30)
src_menu.place(x=40, y=50)

tk.Label(root, text="To Language:", bg="#f2f2f2", font=font_style).place(x=400, y=20)
tgt_menu = ttk.Combobox(root, textvariable=tgt_lang_var, values=lang_names, width=30)
tgt_menu.place(x=400, y=50)

# Input text
tk.Label(root, text="Input Text:", bg="#f2f2f2", font=font_style).place(x=40, y=90)
input_text = tk.Text(root, height=7, width=85, font=("Segoe UI", 10))
input_text.place(x=40, y=115)

# Buttons
translate_btn = tk.Button(root, text="Translate", command=translate_text, bg="#4CAF50", fg="white", width=15, font=("Segoe UI", 10, "bold"))
translate_btn.place(x=300, y=230)

copy_btn = tk.Button(root, text="Copy", command=copy_to_clipboard, bg="#2196F3", fg="white", width=10, font=("Segoe UI", 10))
copy_btn.place(x=280, y=270)

clear_btn = tk.Button(root, text="Clear", command=clear_all, bg="#f44336", fg="white", width=10, font=("Segoe UI", 10))
clear_btn.place(x=390, y=270)

# Output text
tk.Label(root, text="Translated Text:", bg="#f2f2f2", font=font_style).place(x=40, y=320)
output_text = tk.Text(root, height=7, width=85, font=("Segoe UI", 10), bg="#eaeaea", state='disabled')
output_text.place(x=40, y=345)

root.mainloop()
