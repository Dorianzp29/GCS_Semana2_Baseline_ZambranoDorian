# SDD v1 - Diseño del Sistema (STAR-Civil)

## Arquitectura simple
El sistema se plantea como una solución con separación básica:
- Interfaz: uso por ciudadanos y operadores.
- Lógica: reglas de turnos y validaciones.
- Datos: almacenamiento de ciudadanos, turnos y auditoría.

## Componentes principales
1) Ciudadanos: registra y consulta por número de cédula.
2) Turnos: agenda, consulta, cancela y cambia estado (pendiente/atendido/no presentado).
3) Trámites: catálogo (cédula, pasaporte, certificados).
4) Agencias: lista de agencias y horarios.
5) Auditoría: historial de acciones sobre turnos.

## Decisiones técnicas
- Se versionan SRS y SDD como CI principales.
- Se incluye build mínima en /src para reproducibilidad.
- Se incluye config.example para demostrar control de configuración sin exponer secretos.
