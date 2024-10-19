from odoo import models, fields



class StockPicking(models.Model):
    _inherit = "stock.picking"
    distpacher = fields.Char(string="Despachante")






