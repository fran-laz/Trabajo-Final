usuarios = ["ana", "luis", "maria"]
conversaciones = {}

def iniciar_conversacion(usuario1, usuario2):
    clave = tuple(sorted([usuario1, usuario2]))
    if clave not in conversaciones:
        conversaciones[clave] = []
        print(f"Se ha iniciado una nueva conversación entre {usuario1} y {usuario2}")
    else:
        print(f"Reanudando conversación entre {usuario1} y {usuario2}")
    return clave

def enviar_mensaje(conversacion, emisor, mensaje):
    conversaciones[conversacion].append((emisor, mensaje))
    print(f"{emisor} dijo: {mensaje}")
