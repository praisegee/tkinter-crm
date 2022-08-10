from email.mime import image
import tkinter as tk
import _tkinter
from PIL import ImageTk, Image


# window
window = tk.Tk()

window.title("CRM")
window.geometry("600x600")
window.resizable(width=False,height=False)

# logo
# with open("logo - Copy.jpeg", "w") as logos:
#     # print(logos)
#     logo = tk.Canvas
#     real_logo = logo.create_image(image=logos ,x=250,y=100)
#     # real_logo.place()
frame = tk.Frame(width=10, height=10)
frame.place(anchor="s", relx=0.5, rely=0.35)
logo = ImageTk.PhotoImage(Image.open("logo2.jpeg"))
label = tk.Label(frame, image=logo)
label.pack()
# canvas = tk.Canvas(width=400, height=200)
# canvas.place(x=250,y=250)




# image = "a.png"
# logo = tk.PhotoImage(file=image)

# canvas = tk.Canvas()
# canvas.create_image(500, 500)
# canvas.place(x=0, y=0)

# login logo
log_logo = tk.Label(text=" LOGIN ",font=("arial", 10, "bold"), bg="#bdbdbd")
log_logo.place(anchor="s", x=300,y=240)

# username
username = tk.Label(text="username:", font=("areial", 10), bg="#bdbdbd")
username.place(x=150, y=270)

user =tk.Entry()
user.place(x=220,y=270) 
# password

password = tk.Label(text="password:", font=("areial", 10), bg="#bdbdbd")
password.place(x=150,y=300)
passer = tk.Entry()
passer.place(x=220,y=300)
# login
login = tk.Button(text=" Login ", bg="#bdbdbd")
login.place(x=150,y=380)

# register
register = tk.Button(text=" register ",bg="#bdbdbd")
register.place(x=350,y=380)

window.config(bg="#bdbdbd")

window.mainloop()
