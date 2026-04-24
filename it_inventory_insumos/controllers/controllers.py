# -*- coding: utf-8 -*-
# from odoo import http


# class ItInventoryInsumos(http.Controller):
#     @http.route('/it_inventory_insumos/it_inventory_insumos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/it_inventory_insumos/it_inventory_insumos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('it_inventory_insumos.listing', {
#             'root': '/it_inventory_insumos/it_inventory_insumos',
#             'objects': http.request.env['it_inventory_insumos.it_inventory_insumos'].search([]),
#         })

#     @http.route('/it_inventory_insumos/it_inventory_insumos/objects/<model("it_inventory_insumos.it_inventory_insumos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('it_inventory_insumos.object', {
#             'object': obj
#         })
