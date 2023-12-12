import tkinter as tk
from tkinter import filedialog, simpledialog, colorchooser
import os
import tkinter.messagebox as messagebox
import webbrowser





def create_new_file(self):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, 'w') as f:

            pass
        messagebox.showinfo("File Created", "New file created successfully!")
        webbrowser.open("index.html")


class EditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("StickyPawn V 1.0")


        self.text_frame = tk.Frame(self.root)
        self.text_frame.pack(fill="both", expand=True)

        self.line_numbers = tk.Text(self.text_frame, width=4)
        self.line_numbers.pack(side='left', fill='y')

        self.scrollbar = tk.Scrollbar(self.text_frame)
        self.scrollbar.pack(side='right', fill='y')

        self.text_area = tk.Text(self.text_frame,
                                 yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text_area.yview)
        self.text_area.pack(side='left', fill="both", expand=True)

        self.text_area.bind('<<Change>>', self.update_line_numbers)
        self.text_area.bind('<Configure>', self.update_line_numbers)
        self.text_area.bind('<Key>', self.update_line_numbers)

        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.file_menu)

        self.file_menu.add_command(label="Reminder Pad", command=self.open_console)

        self.file_menu.add_command(label="Preferences", command=self.add_properties)    #editor preferences

        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)

        self.settings_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Settings", menu=self.settings_menu)

        self.settings_menu.add_command(label="Change text size",
                                       command=self.change_text_size)
        self.settings_menu.add_command(label="Change text color",
                                       command=self.change_text_color)

        self.folder_inspector_frame = tk.Frame(self.root)
        self.folder_inspector_frame.pack(side='bottom', fill='x')

        self.folder_label = tk.Label(self.folder_inspector_frame,
                                     text="Folder Inspector")
        self.folder_label.pack(side='left')

        self.folder_button = tk.Button(self.folder_inspector_frame,
                                       text="Open Folder",
                                       command=self.open_folder)
        self.folder_button.pack(side='left')

        self.new_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="New", menu=self.new_menu)

        self.new_menu.add_command(label="New Note", command=self.create_new_pawn_file)

        self.var_counter = 0

    def create_var_slot(self):
        self.var_counter += 1
        self.var_menu.add_command(label=f"var {self.var_counter}")

    def update_line_numbers(self, event=None):
        line_numbers = ""
        for i in range(1, int(self.text_area.index('end').split('.')[0])):
            line_numbers += str(i) + '\n'
        self.line_numbers.config(state='normal')
        self.line_numbers.delete('1.0', 'end')
        self.line_numbers.insert('1.0', line_numbers)
        self.line_numbers.config(state='disabled')

    def open_file(self):
        file_path = filedialog.askopenfilename()
        for line in open(file_path):
            self.text_area.insert('end', line)

    def preference_file(self):
       pass

    def save_file(self):
        f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if f is None:
            return
        text2save = str(self.text_area.get(1.0, "end"))
        f.write(text2save)
        f.close()

    def change_text_size(self):
        size = simpledialog.askinteger('Change Text Size',
                                       'Enter new text size:',
                                       minvalue=10,
                                       maxvalue=100)
        if size:
            self.text_area.config(font=("TkDefaultFont", size))

    def change_text_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.text_area.config(fg=color)

    def open_folder(self):
        folder_path = filedialog.askdirectory()
        files = os.listdir(folder_path)
        self.text_area.delete(1.0, "end")
        for file in files:
            self.text_area.insert('end', file + '\n')

    def create_new_file(self):
        # not used yet
        pass

    def create_new_folder(self):
        # not used yet
        pass

    def create_new_pawn_file(self):
        self.text_area.delete(1.0, "end")
        self.text_area.insert("end", "# This is a new note.\n")

    messagebox.showinfo("Popup", "StickyPawn Text Editor Made To Be Basic")  # Show popup message

    def open_console(self):
        console = tk.Toplevel(self.root)
        console_frame = tk.Frame(console)
        console_frame.pack(fill="both", expand=True)
        console_text = tk.Text(console_frame)
        console_text.pack(side='left', fill="both", expand=True)
        console_scrollbar = tk.Scrollbar(console_frame)
        console_scrollbar.pack(side='right', fill='y')
        console_text.config(yscrollcommand=console_scrollbar.set)
        console_scrollbar.config(command=console_text.yview)
        console_text

    def add_properties(self):
        properties_window = tk.Toplevel(self.root)
        properties_frame = tk.Frame(properties_window)
        properties_frame.pack()

        size_label = tk.Label(properties_frame, text="Size")
        size_label.pack()
        size_entry = tk.Entry(properties_frame)
        size_entry.pack()

        x_label = tk.Label(properties_frame, text="X")
        x_label.pack()
        x_entry = tk.Entry(properties_frame)
        x_entry.pack()

        y_label = tk.Label(properties_frame, text="Y")
        y_label.pack()
        y_entry = tk.Entry(properties_frame)
        y_entry.pack()

        save_button = tk.Button(properties_frame, text="Save",
                                command=lambda: self.save_properties(size_entry, x_entry, y_entry))
        save_button.pack()

    def save_properties(self, size_entry, x_entry, y_entry):
        size_value = size_entry.get()
        x_value = x_entry.get()
        y_value = y_entry.get()

        # saving here


root = tk.Tk()
app = EditorApp(root)
root.mainloop()