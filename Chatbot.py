print("¿Sobre qué ciudad quieres información?")
print("La Paz")
print("Cochabamba")
print("Santa Cruz")

opcion = input("Elige una opción :")

if opcion == "La Paz":
    print("📍 LA PAZ\n- Sede de gobierno de Bolivia.\n- Ubicada a más de 3600 metros sobre el nivel del mar.\n- Conocida por su topografía montañosa y el teleférico más alto del mundo.\n- Clima frío de altiplano, con temperaturas frescas todo el año.")
elif opcion == "Cochabamba":
    print("📍 COCHABAMBA\n- Conocida como 'la ciudad de la eterna primavera'.\n- Ubicada en el valle central de Bolivia.\n- Famosa por su gastronomía y el Cristo de la Concordia.\n- Clima templado con temperaturas agradables durante casi todo el año.")
elif opcion == "Santa Cruz":
    print("📍 SANTA CRUZ\n- Ciudad más poblada y motor económico del país.\n- Ubicada en el oriente boliviano, en la llanura tropical.\n- Famosa por su desarrollo industrial y su cultura camba.\n- Clima cálido y húmedo, con lluvias frecuentes en verano.")
else:
    print("Opción no válida.")
