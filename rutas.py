# Lugares turísticos de Bolivia
lugares_bolivia = [
    "Salar de Uyuni",
    "Potosí (Ciudad Imperial)",
    "Sucre (Ciudad Blanca)",
    "La Paz (Teleférico Urbano)",
    "Copacabana (Lago Titicaca)",
    "Tiwanaku (Ruinas Arqueológicas)",
    "Santa Cruz (Jardín Botánico)",
    "Rurrenabaque (Puerta a la Amazonía)"
]

def crear_ruta():
    print("\n=== CREAR RUTA TURÍSTICA EN BOLIVIA ===")
    print("Lugares disponibles:")
    for i, lugar in enumerate(lugares_bolivia, 1):
        print(f"{i}. {lugar}")
    
    seleccion = input("\nIngrese números de lugares separados por comas (ej: 1,3,5): ")
    try:
        indices = [int(i)-1 for i in seleccion.split(",")]
        ruta = [lugares_bolivia[i] for i in indices if 0 <= i < len(lugares_bolivia)]
        
        if ruta:
            print("\n✔ Ruta creada:")
            print(" → ".join(ruta))
        else:
            print("\n✖ No se seleccionaron lugares válidos")
    except:
        print("\n✖ Error: Ingrese números válidos")

# Ejecutar
if __name__ == "__main__":
    crear_ruta()