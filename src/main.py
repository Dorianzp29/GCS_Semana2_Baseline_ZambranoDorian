from datetime import datetime

ciudadanos = {}
turnos = []

def registrar_ciudadano(cedula, nombres, apellidos, telefono, correo):
    if cedula in ciudadanos:
        raise ValueError("Ciudadano ya registrado.")
    ciudadanos[cedula] = {
        "nombres": nombres,
        "apellidos": apellidos,
        "telefono": telefono,
        "correo": correo
    }

def agendar_turno(cedula, tramite, agencia, fecha_hora):
    if cedula not in ciudadanos:
        raise ValueError("Ciudadano no registrado.")
    codigo = f"T-{len(turnos)+1:04d}"
    turnos.append({
        "codigo": codigo,
        "cedula": cedula,
        "tramite": tramite,
        "agencia": agencia,
        "fecha_hora": fecha_hora,
        "estado": "PENDIENTE"
    })
    return codigo

def listar_turnos_por_cedula(cedula):
    return [t for t in turnos if t["cedula"] == cedula]

def main():
    registrar_ciudadano("1712345678", "Juan", "Perez", "0999999999", "juan@mail.com")

    codigo = agendar_turno(
        "1712345678",
        "Cedulación",
        "Agencia Santo Domingo",
        datetime(2026, 2, 1, 10, 0)
    )

    print("Turno creado:", codigo)
    print("Turnos del ciudadano:", listar_turnos_por_cedula("1712345678"))

if __name__ == "__main__":
    main()
