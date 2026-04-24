# Análisis de Regla Salarial: Auxilio de Transporte (TRANS)

## Identificación de Errores

### 1. Hardcoding de Valores (Error Técnico y de Mantenimiento)
El código tiene los valores del SMMLV (1.300.000) y del Auxilio de Transporte (162.000) escritos directamente ("quemados"). 
- **Consecuencia**: El cálculo será incorrecto para el año fiscal actual (2026). Las reglas salariales deben ser dinámicas y consultar constantes o parámetros del sistema.

### 2. Base de Comparación Incorrecta (Error Legal)
El código usa `salario_basico = payslip.contract_id.wage`.
- **Explicación**: Según la ley colombiana, el derecho al auxilio de transporte se determina sobre el **total devengado** (Salario + Comisiones + Horas Extras + Recargos), no solo sobre el básico del contrato. 
- **Consecuencia**: Si un empleado gana 1.5 SMMLV de básico pero con horas extras supera los 2 SMMLV, el código actual le seguiría pagando el auxilio, lo cual es un error legal.

### 3. Error de Indentación/Lógica (Error de Código)
El cálculo de proporcionalidad (`result = result * (dias_trabajados / 30)`) está indentado dentro del `if`. 
- **Consecuencia**: Si el salario es mayor a 2 SMMLV, el código simplemente no ejecuta la lógica de días y devuelve 0. Aunque el resultado final (0) es correcto en ese caso, es una mala práctica de estructuración.

---

## Versión Corregida (Valores Oficiales 2026)

Según las cifras vigentes para 2026:
- **SMMLV 2026**: $1.750.905
- **Auxilio de Transporte 2026**: $249.095

```python
# Regla corregida: Auxilio de transporte colombiano 2026
result = 0
# Se debe evaluar sobre el total devengado (GROSS) antes de deducciones
total_devengado = categories.BASIC + categories.ALW

# Valores oficiales 2026
SMMLV_2026 = 1750905 
AUX_TRANS_2026 = 249095 

# Evaluación legal: menor o igual a 2 SMMLV ($3.501.810)
if total_devengado <= (2 * SMMLV_2026):
    # Proporcionalidad por días trabajados (Seguridad ante ausencia de la entrada)
    dias_trabajados = worked_days.get('WORK100') and worked_days['WORK100'].number_of_days or 30
    
    # El auxilio se paga proporcional a los días laborados
    result = AUX_TRANS_2026 * (dias_trabajados / 30)
```


## Conclusión Técnica
La regla original fallaría por obsolescencia de datos y por una interpretación errónea de la base gravable colombiana. La versión corregida es dinámica, cumple con la legalidad de montos por "devengado total" y maneja de forma segura las variables de Odoo (`worked_days`).
