# Prueba Técnica: Desarrollador Odoo - Maxialimentos SAS
**Candidato:** Wilson Mauricio Rodriguez Rodriguez

**Tecnología:** Odoo 16.0 Community Edition

---

## Organización del Repositorio
Para facilitar la revisión, el proyecto se ha dividido de la siguiente manera:

1.  **`/it_inventory_insumos`**: Carpeta del módulo desarrollado para Odoo 16. Contiene toda la lógica de modelos, vistas y seguridad solicitada en el **Ejercicio 1**.
2.  **`analisis_nomina.md`**: Documento con la resolución del **Ejercicio 2**, identificando errores técnicos y legales en las reglas salariales.
3.  **`propuestas_solucion.md`**: Documento con las propuestas arquitectónicas para los 5 casos de negocio del **Ejercicio 3**.
4.  **`README.md`**: Este archivo, con la descripción general y decisiones técnicas.

---

## Ejercicio 1: Control de Insumos IT
Se ha desarrollado un módulo para centralizar el inventario de mantenimientos de IT.
*   **Alerta Visual**: Se implementó una lógica dinámica en la vista de lista que resalta en **rojo** los insumos cuando su stock es inferior al mínimo definido.
*   **Trazabilidad**: Se incluyeron campos de Sede y Categoría para cumplir con el requerimiento de reporte por ubicación.
*   **Integración**: Relación directa con el maestro de proveedores (`res.partner`) de Odoo.

## Ejercicio 2: Análisis de Nómina Colombia
Se realizó la corrección de la regla salarial de Auxilio de Transporte proyectada a **2026**, corrigiendo el error de "valores quemados" y asegurando que el cálculo se base en el **Total Devengado** y no solo en el básico, cumpliendo con la ley colombiana.

## Ejercicio 3: Propuestas de Solución
Se plantean soluciones para casos reales (POS, Facturación DIAN, Logística y Gestión de proyectos) enfocadas en la eficiencia y el uso de herramientas nativas de Odoo y Odoo.sh.

---

### Instrucciones de Instalación (Módulo)
1. Copiar la carpeta `it_inventory_insumos` en tu directorio de addons.
2. Instalar el módulo desde el menú de Aplicaciones en Odoo 16.
3. El módulo depende de `base` y `stock`.

*Desarrollado bajo Python 3.10.*
