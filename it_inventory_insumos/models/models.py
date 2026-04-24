# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ItInventoryInsumos(models.Model):

    """
    Modelo para la gestion de insumos de IT.
    Permite el control de stock por sede y categoria con alertas visuales.
    """

    _name = 'it.inventory.insumo'
    _description = 'Inventario de insumos de mantenimiento IT'

    #  Campos basicos con labels claros para el usuario final.
    name = fields.Char(string='Nombre del insumo', required=True,
    help="Nombre descriptivo del insumo")


    #  Campo de seleccion para tipificar el insumo
    category = fields.Selection([
        ('tonner', 'Tonner'),
        ('cable', 'Cable'),
        ('repuesto', 'Repuesto'),
        ('herramienta', 'Herramienta'),
        ('otro', 'Otro')
    ], string='Categoria', default="otro", required=True)


    # Identificacion de la sede para seguir la trazabilidad
    sede = fields.Selection([
        ('bogota', 'Bogota Principal'),
        ('sede2', 'Sede 2'),
        ('san_martin', 'San Martin'),
        ('granada', 'Dranada CILA')
    ], string='Sede', required=True)

    # Campos numericos para el control del inventario
    qty_stock = fields.Float(string='Cantidad en Stock', default=0.0)
    qty_min_alert = fields.Float(string='Cantidad Minima Alerta', default=0.0)
    price_unit = fields.Float(string='Precio Unitario')
    
    # Relacion con el modelo res.partner para obtener el proveedor
    partner_id = fields.Many2one('res.partner', string='Proveedor')
    
    