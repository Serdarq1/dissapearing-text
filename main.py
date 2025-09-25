import tkinter as tk
import os

class DissaperingText:
    def __init__(self):
        self.tk = tk.Tk()
        self.tk.title("Dissapering Text")
        self.tk.geometry("600x350")
        self.my_var = tk.StringVar()
        self.my_var.trace_add('write', self.on_change)

        self.wait_time_ms = 5000
        self.after_id = None

        self.start_time = None
        self.ui()
        self.tk.mainloop()

    def on_change(self, *args):
        if self.after_id:
            self.tk.after_cancel(self.after_id)
        self.after_id = self.tk.after(self.wait_time_ms, self.dissapear_text)


    def ui(self):
        """Sets the UI up"""
        self.input = tk.Label(self.tk, text="Start Typing: ", font=("Arial", 18, "bold"))
        self.label = tk.Label(self.tk, text="Your text will dissapear in 5 seconds if you stop writing.", font=("Arial", 14, "italic"))
        self.input.pack(pady=20)
        self.label.pack(pady=5)
        self.text = tk.Entry(self.tk, width=50, textvariable=self.my_var)
        self.text.pack(pady=10, ipady=6)

        self.save_btn = tk.Button(text='Save', font=("Arial", 14), command=self.save_text)
        self.save_btn.pack(pady=20)


    def dissapear_text(self):
        """Dissapears text"""
        self.text.delete(0, tk.END)

    def save_text(self):
        """Saves the written text"""
        path = os.path.join(os.path.dirname(__file__), "text.txt")
        with open(path, mode="a+", encoding="utf-8") as f:
            f.seek(0)               
            cont = f.read()
            text_to_write = ("" if cont == "" else "\n") + self.text.get()
            f.write(text_to_write)
        self.my_var.set("")         

        

DissaperingText()