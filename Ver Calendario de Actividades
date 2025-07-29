calendario = [
    {"fecha": "2025-07-30", "actividad": "Reunión de equipo"},
    {"fecha": "2025-07-31", "actividad": "Entrega de proyecto"},
    {"fecha": "2025-08-01", "actividad": "Capacitación"}
]

def ver_calendario(filtro_fecha=None):
    print("=== Calendario de Actividades ===")
    eventos_filtrados = calendario
    if filtro_fecha:
        eventos_filtrados = [e for e in calendario if e["fecha"] == filtro_fecha]

    if eventos_filtrados:
        for evento in eventos_filtrados:
            print(f"{evento['fecha']}: {evento['actividad']}")
    else:
        print("No hay actividades para la fecha seleccionada.")
