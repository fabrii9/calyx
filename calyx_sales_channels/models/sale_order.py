from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"

    detail = fields.Char(string="Detalle")
    def action_confirm(self):
        if self.validity_date != False:
            super().action_confirm()