import bdb
from tkinter import *
from app import get_response, bot_name

BG_WHITE = "#ffffff"
BG_COLOR = "#bababa"
TEXT_COLOR = "#000000"
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

class ChatApplication:
    
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
        
    def run(self):
        self.window.mainloop()
        
    def _setup_main_window(self):
        self.window.title("Healthbot")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg="#5F6A6A")
        
        head_label = Label(self.window, bg="#85929E", fg="#ffffff",text="Welcome! I am COVID-19 Healthbot", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)
        
        line = Label(self.window, width=450, bg="#5D6D7E", bd=0)
        line.place(relwidth=1, rely=0.07, relheight=0.012)
        
        self.text_widget = Text(self.window, width=19, height=2, bg="#ffffff", fg=TEXT_COLOR,font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.825, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=2)
        scrollbar.configure(command=self.text_widget.yview)
        
        bottom_label = Label(self.window, bg="#2C3E50", height=40)
        bottom_label.place(relwidth=1, rely=0.9)
        
        self.msg_entry = Entry(bottom_label, bg="#566573", fg="#000000", font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
        send_button = Button(bottom_label, text="Send",fg="#ffffff", font=FONT_BOLD, width=20, bg="#58D68D",command=lambda: self._on_enter_pressed())
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
     
    def _on_enter_pressed(self):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")
        
    def _insert_message(self, msg, sender):
        if not msg:
            return
        
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        
        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        
        self.text_widget.see(END)
             
        
if __name__ == "__main__":
    app = ChatApplication()
    app.run()