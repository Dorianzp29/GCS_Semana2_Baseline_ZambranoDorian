# SRS v1 - Sistema de Turnos y Atención del Registro Civil (STAR-Civil)

## Requisitos funcionales (RF)
RF-01: El sistema debe permitir registrar los datos básicos del ciudadano (cédula, nombres, apellidos, teléfono, correo).
RF-02: El sistema debe permitir agendar un turno seleccionando trámite, agencia, fecha y hora disponible.
RF-03: El sistema debe permitir consultar los turnos agendados usando el número de cédula.
RF-04: El sistema debe permitir cancelar un turno antes de la fecha programada y liberar el cupo.
RF-05: El sistema debe generar un comprobante de turno con código único y datos del trámite.
RF-06: El sistema debe permitir que el operador marque un turno como “Atendido” o “No se presentó”.

## Requisitos no funcionales (RNF)
RNF-01: El sistema debe mantener un registro de auditoría de creación, cancelación y atención de turnos.
RNF-02: El sistema debe asegurar estabilidad en ejecución local para evitar pérdida de turnos por fallos.
