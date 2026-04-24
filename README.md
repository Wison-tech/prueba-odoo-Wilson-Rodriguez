# Prueba Técnica: Desarrollador Odoo - Maxialimentos SAS
**Candidato:** Wilson Mauricio Rodriguez Rodriguez 

**Tecnología:** Odoo 16.0 Community Edition

## Ejercicio 1: Módulo de Control de Insumos IT (`it_inventory_insumos`)

### Descripción de la Solución
Se ha desarrollado un módulo personalizado para centralizar y controlar el inventario de insumos de mantenimiento de equipos de cómputo. La solución sustituye el registro manual (papel) por un sistema digital con trazabilidad completa por sede y alertas automáticas de reabastecimiento.

### Estructura del Módulo
La organización del código sigue los estándares de Odoo:
- `models/`: Definición de la lógica de negocio y estructura de datos en PostgreSQL.
- `views/`: Definición de interfaces de usuario (formularios y listas).
- `security/`: Control de accesos y permisos.
- `__manifest__.py`: Metadata, dependencias y registro de archivos de carga.

### Decisiones Técnicas y Criterio Profesional
1. **Modelo de Datos**: Se optó por una clase heredada de `models.Model` para persistencia total. 
2. **Campos de Selección (Selection)**: Para los campos `category` y `sede`, se utilizaron diccionarios de selección dinámicos para garantizar la integridad de los datos y facilitar el filtrado de registros.
3. **Integración con Nucleo Odoo**: Se implementó una relación `Many2one` con el modelo estándar `res.partner`. Esto permite aprovechar la base de datos de proveedores existente en Odoo sin duplicar información.
4. **Alerta de Stock (UX/UI)**: Para cumplir con el requerimiento de indicadores visuales, se utilizó el atributo `decoration-danger` en la vista de lista (`tree`). Esta técnica es preferida sobre cálculos en el cliente porque se procesa eficientemente en el servidor y ofrece una respuesta visual inmediata.
5. **Documentación de Código**: Todo el código fuente cuenta con docstrings y comentarios explicativos para facilitar el mantenimiento por parte del equipo de IT de Maxialimentos.



---
*Este proyecto fue desarrollado bajo un entorno de Python 3.10 cumpliendo con los estándares de rendimiento de Odoo 16.*
