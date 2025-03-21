from tkinter import *
from tkinter import messagebox
import base64

def decrypt():
    password = code.get()

    if password == "1234":
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message = text1.get(1.0, END).strip()
        try:
            # Decode the base64-encoded message
            decode_message = base64.b64decode(message.encode("ascii"))
            decrypt_text = decode_message.decode("ascii")

            Label(screen2, text="DECRYPT", font="arial 12 bold", fg="white", bg="#00bd56").place(x=10, y=0)
            text2 = Text(screen2, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
            text2.place(x=10, y=40, width=380, height=150)

            text2.insert(END, decrypt_text)
            text2.config(state=DISABLED)  # Make the text box read-only
        except Exception as e:
            messagebox.showerror("Error", "Invalid input for decryption!")
    elif password == "":
        messagebox.showerror("Decryption", "Input Password")
    else:
        messagebox.showerror("Decryption", "Invalid Password")


def encrypt():
    password = code.get()

    if password == "1234":
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message = text1.get(1.0, END).strip()
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt_text = base64_bytes.decode("ascii")

        Label(screen1, text="ENCRYPT", font="arial 12 bold", fg="white", bg="#ed3833").place(x=10, y=0)
        text2 = Text(screen1, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, encrypt_text)
        text2.config(state=DISABLED)  # Make the text box read-only
    elif password == "":
        messagebox.showerror("Encryption", "Input Password")
    else:
        messagebox.showerror("Encryption", "Invalid Password")


def main_screen():
    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("375x398")
    screen.resizable(False, False)

    # Icon
    image_icon = PhotoImage(file="C:/Users/HP/Downloads/VIPS_Logo.png")
    screen.iconphoto(False, image_icon)
    screen.title("EncDecApp")

    def reset():
        code.set("")
        text1.delete(1.0, END)

    Label(screen, text="Enter text for encryption and decryption", fg="black", font=("Calibri", 13)).place(x=10, y=10)
    text1 = Text(screen, font="Roboto 12", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=335, height=100)

    Label(screen, text="Enter secret key for encryption", fg="black", font=("Calibri", 13)).place(x=10, y=170)

    code = StringVar()
    Entry(screen, textvariable=code, width=19, bd=0, font=("Arial", 25), show="*").place(x=10, y=200)

    Button(screen, text="ENCRYPT", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(screen, text="DECRYPT", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(screen, text="RESET", height="2", width=50, bg="#1089ff", fg="white", bd=0, command=reset).place(x=10, y=300)

    screen.mainloop()


main_screen()
