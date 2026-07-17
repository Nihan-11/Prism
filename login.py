import customtkinter as ctk
from PIL import Image
from pathlib import Path
import serverconnect


# ---------------- Settings ----------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ---------------- App ----------------
serverconnect.dbpassword_requestui() 
 # Call the function to request the database password
class Login(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Login")
        self.geometry("800x500")
        self.resizable(False, False)
        self.configure(fg_color="#0d0f15")

        self.create_widgets()

    def create_widgets(self):

        # ---------- Left Image ----------

        image_path = Path("image1.png")

        if image_path.exists():
            image = Image.open(image_path)

            image_label = ctk.CTkLabel(
                self,
                text="",
                image=ctk.CTkImage(
                    light_image=image,
                    dark_image=image,
                    size=(400, 500)
                )
            )
        else:
            image_label = ctk.CTkLabel(
                self,
                text="Image Not Found",
                width=400,
                height=500,
                fg_color="#1a1d26",
                text_color="white"
            )

        image_label.place(x=0, y=0)

        # ---------- Title ----------

        ctk.CTkLabel(
            self,
            text="Welcome Back!",
            font=("Arial", 30, "bold")
        ).place(x=500, y=40)

        # ---------- Username ----------

        ctk.CTkLabel(
            self,
            text="Username",
            font=("Arial", 18)
        ).place(x=450, y=120)

        self.username = ctk.CTkEntry(
            self,
            width=300,
            placeholder_text="Enter username"
        )
        self.username.place(x=450, y=150)

        # ---------- Password ----------

        ctk.CTkLabel(
            self,
            text="Password",
            font=("Arial", 18)
        ).place(x=450, y=220)

        self.password = ctk.CTkEntry(
            self,
            width=300,
            placeholder_text="Enter password",
            show="*"
        )
        self.password.place(x=450, y=250)

        # ---------- Checkboxes ----------

        self.remember = ctk.CTkCheckBox(
            self,
            text="Remember Me"
        )
        self.remember.place(x=450, y=310)

        self.new_user = ctk.CTkCheckBox(
            self,
            text="I'm New"
        )
        self.new_user.place(x=450, y=340)

        # ---------- Login Button ----------

        ctk.CTkButton(
            self,
            text="Login",
            width=300,
            command=self.login
        ).place(x=450, y=400)

    def login(self):
        username = self.username.get()
        password = self.password.get()
        is_new_user = self.new_user.get()


        if is_new_user:
            #intiate new user protocol
            serverconnect.new_userprotocol()
            #insert new user into database
            serverconnect.insert_user(username, password)
        if not is_new_user:
            #check if user exists in database
            print("Checking user credentials...")
            print(f"Username: {username}, Password: {password}")
            if serverconnect.user_exists(username, password):
                print("Login successful!")
            else:
                print("Login failed! User does not exist or incorrect password.")



# ---------------- Run ----------------

if __name__ == "__main__":
    app = Login()
    app.mainloop()