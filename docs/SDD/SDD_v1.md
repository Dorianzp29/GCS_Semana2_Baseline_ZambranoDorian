# SDD v1 - Diseño del Sistema (STAR-Civil)

## Arquitectura simple
- Interfaz: ciudadano y operador.
- Lógica: reglas de turnos, validaciones y estados.
- Datos: almacenamiento de ciudadanos, turnos y auditoría.

## Componentes
1) Ciudadanos: registro y consulta por cédula.
2) Turnos: agendar, consultar, cancelar y actualizar estado.
3) Trámites: catálogo de servicios (cédula, pasaporte, certificados).
4) Agencias: agencias disponibles y horarios.
5) Auditoría: historial de acciones del sistema.

## Decisiones técnicas
- Documentos SRS y SDD se controlan como CI.
- Se incluye build mínima para reproducibilidad.
- Se separa configuración en /config con ejemplo sin secretos.
