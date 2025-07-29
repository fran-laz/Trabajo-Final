lugares_disponibles = ["Valle de la Luna", "Cristo de la Concordia", "Biocentro Güembé", "Teleférico", "Plaza 24 de Septiembre"]

favoritos = []

print("⭐ Marcar lugar como favorito")
print("Lugares disponibles:")
for i, lugar in enumerate(lugares_disponibles, start=1):
    print(f"{i}. {lugar}")

opcion = input("\nEscribe el nombre del lugar que deseas marcar como favorito: ").strip()

if opcion in favoritos:
    print("⚠️ Este lugar ya está en tu lista de favoritos.")
elif opcion in lugares_disponibles:
    favoritos.append(opcion)
    print(f"✅ '{opcion}' fue añadido a tu lista de favoritos.")
else:
    print("❌ El lugar no existe en la lista de lugares disponibles.")

if favoritos:
    print("\n⭐ Tus lugares favoritos:")
    for fav in favoritos:
        print(f"- {fav}")
else:
    print("\n(No tienes lugares marcados como favoritos aún.)")
