
usuarios = {
    "kendry": "kendry",
    "ezel": "ezel",
    "gabo": "gabo"
}

def iniciar_sesion():
    print("\n=== INICIAR SESIÓN ===")
    print("Usuarios registrados:", ", ".join(usuarios.keys()))
    
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")
    
    if usuario in usuarios and usuarios[usuario] == clave:
        print(f"\n✔ ¡Bienvenido/a, {usuario}!")
        return True
    else:
        print("\n✖ Usuario o clave incorrectos")
        return False


if __name__ == "__main__":
    iniciar_sesion()