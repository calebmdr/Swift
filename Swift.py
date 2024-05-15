import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Swift Text Editor")
        self.master.iconbitmap("icon.ico")  # Set the icon
        self.textarea = tk.Text(self.master, wrap="word")
        self.textarea.pack(expand=True, fill="both")
        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self.master)
        
        # File Menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        
        # Edit Menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Cut", command=self.cut)
        edit_menu.add_command(label="Copy", command=self.copy)
        edit_menu.add_command(label="Paste", command=self.paste)
        menubar.add_cascade(label="Edit", menu=edit_menu)

        # Help Menu
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)
        
        self.master.config(menu=menubar)

    def new_file(self):
        self.textarea.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                text = file.read()
            self.textarea.delete(1.0, tk.END)
            self.textarea.insert(1.0, text)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            text = self.textarea.get(1.0, tk.END)
            with open(file_path, "w") as file:
                file.write(text)

    def cut(self):
        self.textarea.event_generate("<<Cut>>")

    def copy(self):
        self.textarea.event_generate("<<Copy>>")

    def paste(self):
        self.textarea.event_generate("<<Paste>>")

    def show_about(self):
        messagebox.showinfo("About", "Swift Text Editor\nVersion 1.0\nby CM")

def main():
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
