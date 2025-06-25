import customtkinter as ctk

# configurar aparência
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# configuração da janela principal
app = ctk.CTk()
app.title("Sistema de Login")
app.geometry("400x400")

# Criação de funcionalidades
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    # Verificar se o usuário é "Gislayne" e a senha "123456"
    if usuario == "Gislayne" and senha == "123456":
        resultado_login.configure(text="Login feito com sucesso!", text_color="green")
    else:
        resultado_login.configure(text="Login Incorreto", text_color="red")

# Criação de campos usando Label, Entry e Button
label_usuario = ctk.CTkLabel(app, text="Usuário")
label_usuario.pack(pady=10)

campo_usuario = ctk.CTkEntry(app, placeholder_text="Digite seu usuário")
campo_usuario.pack(pady=10)

label_senha = ctk.CTkLabel(app, text="Senha")
label_senha.pack(pady=10)

campo_senha = ctk.CTkEntry(app, placeholder_text="Digite sua senha", show="*")
campo_senha.pack(pady=10)

botao_login = ctk.CTkButton(app, text="Login", command=validar_login)
botao_login.pack(pady=10)

# Feedback do login
resultado_login = ctk.CTkLabel(app, text="")
resultado_login.pack(pady=10)

# Iniciar a aplicação
app.mainloop()
