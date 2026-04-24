# Propuestas de Solución - Maxialimentos SAS

## Caso 1: Alertas de Facturación (DIAN)
**Propuesta:**
Crear un mecanismo que revise automáticamente los números de factura disponibles.
*   **Cómo funciona:** El sistema revisará todos los días la cantidad de números que quedan en la resolución de la DIAN.
*   **La Alerta:** Cuando falte el 10% de los números o queden 30 días para que venza el plazo, Odoo creará una "Actividad Pendiente" en el tablero del contador para que no se le olvide renovarla.
*   **Anticipación:** 30 días antes del vencimiento.

## Caso 2: Límites de precio en la Caja (POS)
**Propuesta:**
Programar un control de seguridad en la pantalla de la caja registradora.
*   **Cómo funciona:** Se añade una regla matemática en la interfaz. Si el cajero intenta poner un precio que supere el límite permitido (ej. $1.000.000 por producto), el sistema bloqueará la venta.
*   **Mensaje:** Aparecerá una ventana que diga: "Monto demasiado alto. Por favor verifique el valor".

## Caso 3: Movimiento entre Bodegas
**Propuesta:**
Configurar rutas de inventario automáticas.
*   **Cómo funciona:** Configuramos la "Sede Norte" para que su fuente de suministro sea la "Sede 2". 
*   **El flujo:** Cuando el cliente compra en Norte, Odoo hace el "traslado interno" desde Sede 2 automáticamente. Solo requiere configuración de los almacenes en el módulo de Inventario estándar.

## Caso 4: Carga de PDFs masiva
**Propuesta:**
Herramienta de carga inteligente.
*   **Cómo funciona:** Creamos un asistente donde el usuario sube un archivo ZIP con todos los documentos. El sistema buscará a cada cliente por su NIT (viendo el nombre del archivo) y adjuntará el PDF en su ficha personal automáticamente.
*   **Beneficio:** Ahorra horas de trabajo manual de estar subiendo uno por uno.

## Caso 5: Criterio de Trabajo
*   **Sobre Odoo.sh:** No se puede trabajar siempre sobre la rama de Staging (emergencia). Mi prioridad en los primeros 5 días sería arreglar el error del módulo `Pedido_peso` en la rama de Desarrollo para que el flujo de trabajo vuelva a la normalidad y sea seguro.
*   **Sobre el retraso en el Sprint:** Hablaría de inmediato con el Director de IT al detectar el problema (Día 8). Propongo terminar 2 de las 3 tareas con calidad total, en lugar de entregar las 3 mal hechas. La transparencia es clave para renegociar los tiempos.
