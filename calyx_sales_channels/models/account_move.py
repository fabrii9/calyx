from odoo import models, fields


class SalesChannels(models.Model):
    _inherit = "sale.order"
    name_channel = fields.Char(string="Nombre del canal de venta", required=True)
    code_channel = fields.Char(string="Código del canal de venta", readonly=True)
    warehouse_channel = fields.Char(string="Almacén del canal de venta")
    journal_channel = fields.Char(string="Diario del canal de venta")








