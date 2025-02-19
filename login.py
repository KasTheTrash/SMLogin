from pathlib import Path
import threading
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,messagebox
import psycopg2
import bcrypt
import subprocess
import sys


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame0")



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def check_login(username, password):
    try:
        # Σύνδεση με τη βάση δεδομένων PostgreSQL
        connection = psycopg2.connect(
            user="postgres",
            password="123456",
            host="localhost",
            port="5432",
            database="StoreManager"
        )
        cursor = connection.cursor()
        
        # Δημιουργία των πινάκων αν δεν υπάρχουν
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(60) NOT NULL
        );
        '''
        cursor.execute(create_table_query)
        connection.commit()

        # Εκτέλεση SQL ερωτήματος για έλεγχο του χρήστη
        cursor.execute("SELECT password FROM users WHERE username = LOWER(%s)", (username,))
        result = cursor.fetchone()
        
        if result and bcrypt.checkpw(password.encode('utf-8'), result[0].encode('utf-8')):
            messagebox.showinfo("Success", "Login successful!")
            window.destroy()  # Κλείσιμο του παραθύρου Tkinter
            subprocess.call(["python", "main.py"])  # Εκκίνηση του main.py
            
            #window.after(100, start_main_script)
            #window.after(500, window.destroy)
            #subprocess.call(["python", "main.py"])
            #sys.exit()
        else:
            messagebox.showerror("Error", "Invalid username or password.")
        
    except (Exception, psycopg2.Error) as error:
        messagebox.showerror("Error", f"Error while connecting to PostgreSQL: {error}")
    
    finally:
        if connection:
            cursor.close()
            connection.close()
            sys.exit()
#cursor.execute("SELECT * FROM users WHERE LOWER(username) = LOWER(%s) AND password = %s", (username, password))


def start_main_script():
    threading.Thread(target=subprocess.call, args=(["python", "main.py"],)).start()


def on_login_button_click():
    username = entry_1.get()
    password = entry_2.get()
    check_login(username, password)

def on_enter_key_pressed_in_name(event):
    entry_2.focus_set()

def on_enter_key_pressed_in_password(event):
    button_1.focus_set()
    on_login_button_click()
window = Tk()
window.geometry("304x450")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 450,
    width = 304,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    304.0,
    49.0,
    fill="#D6D6D6",
    outline="")

canvas.create_text(
    32.0,
    12.0,
    anchor="nw",
    text="StoreManager Pro",
    fill="#000000",
    font=("KronaOne Regular", 20 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))

button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: check_login (entry_1.get(), entry_2.get()), #print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=160.0,
    y=383.0,
    width=128.0,
    height=32.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    132.0,
    156.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#EBEBEB",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=22.0,
    y=92.0,
    width=220.0,
    height=20.0
)
entry_1.bind("<Return>", on_enter_key_pressed_in_name)

canvas.create_text(
    12.0,
    120.0,
    anchor="nw",
    text="Password",
    fill="#000000",
    font=("Inter", 16 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    132.0,
    103.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#EBEBEB",
    fg="#000716",
    highlightthickness=0,
    show="*"
)

entry_2.place(
    x=22.0,
    y=145.0,
    width=220.0,
    height=20.0
)
entry_2.bind("<Return>", on_enter_key_pressed_in_password)


canvas.create_text(
    12.0,
    67.0,
    anchor="nw",
    text="Name",
    fill="#000000",
    font=("Inter", 16 * -1)
)
window.resizable(False, False)
window.mainloop()
