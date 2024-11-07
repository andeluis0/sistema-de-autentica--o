import customtkinter
import customtkinter as ctk
import CTkMessagebox
from CTkMessagebox import CTkMessagebox 



ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
            
  
app = ctk.CTk()
app.title("Tela de Login")
app.geometry("300x500")
app.configure(background="black")


def verificar_login():
    usuario = entry_login.get()
    senha = entry_senha.get()
    
    if usuario == "admin" and senha == "admin123":
        CTkMessagebox(title="Sucesso", message="Login efetuado com sucesso!", icon="check")
   
    elif usuario != "admin":
        CTkMessagebox(title="Erro", message="Usuário não encontrado!", icon="cancel")
   
    elif senha != "admin123":
        CTkMessagebox(title="Erro", message="Senha incorreta!", icon="cancel")






label_login = ctk.CTkLabel(app, text="Usuário:")

label_login.pack(pady=10)

entry_login = ctk.CTkEntry(app, 
                           placeholder_text="Digite seu usuário")
entry_login.pack(pady=10)

label_senha = ctk.CTkLabel(app, text="Senha:")

label_senha.pack(pady=10)

entry_senha = ctk.CTkEntry(app,
                           placeholder_text="Digite sua senha", 
                           show="*")
entry_senha.pack(pady=10)

botao_login = ctk.CTkButton(app, text="Entrar",
                            command=(verificar_login))
botao_login.pack(pady=20)








app.mainloop()