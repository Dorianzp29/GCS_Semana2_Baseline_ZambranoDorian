# GCS Semana 2 - Baseline v1.0 (STAR-Civil)

## Objetivo del proyecto
Este repositorio demuestra cómo organizar elementos de configuración (CI) y establecer una línea base (Baseline v1.0) usando tags y un release, asegurando trazabilidad, auditoría y reproducibilidad.

## Estructura del repositorio
- /docs/SRS: requisitos del sistema
- /docs/SDD: diseño del sistema
- /src: código mínimo versionado
- /tests: pruebas (extensión)
- /config: configuración controlada (ejemplo)
- /scripts: utilidades (opcional)
- CHANGELOG.md: registro de cambios

## Cómo ejecutar
python src/main.py

## Cómo crear la Baseline v1.0
1) Confirmar que SRS + SDD + build estable están completos.
2) Crear tag:
   git tag -a baseline-v1.0 -m "Baseline v1.0 - SRS v1 + SDD v1 + build estable"
3) Subir el tag:
   git push origin baseline-v1.0
4) Crear un Release en GitHub usando ese tag como evidencia.
