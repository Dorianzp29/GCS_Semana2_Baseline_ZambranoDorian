# GCS Semana 2 - Baseline v1.0 (STAR-Civil)

## Objetivo del proyecto
Este repositorio demuestra cómo organizar elementos de configuración (CI) y establecer una línea base (Baseline v1.0) usando tags y un release para mantener trazabilidad, auditoría y reproducibilidad.

## Estructura del repositorio
- /docs/SRS: requisitos del sistema
- /docs/SDD: diseño del sistema
- /src: código mínimo versionado
- /tests: pruebas básicas (placeholder)
- /config: configuración controlada (ejemplo)
- /scripts: utilidades opcionales
- CHANGELOG.md: registro de cambios
- README.md: guía del repositorio

## Cómo ejecutar
python src/main.py

## Cómo crear Baseline v1.0
1) Confirmar que SRS_v1, SDD_v1, src y config.example están listos.
2) Crear tag:
   git tag -a v1.0 -m "Baseline v1.0: SRS+SDD approved + minimal build"
3) Subir tag:
   git push origin v1.0
4) Crear Release v1.0 en GitHub usando el tag.
