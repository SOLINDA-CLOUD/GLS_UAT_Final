from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    # sale_order_ids = fields.One2many('sale.order', 'partner_id', 'Sales Order')

    # @api.depends(sale_order_ids.partner_id)
    # def _compute_total_sales(self):
    #     pass

    # Customer Management Scoring
    omset = fields.Float(string='Omset', store=True)
    payment_history = fields.Float(string='History of Payment')
    communication = fields.Selection([
        ('too_slow', 'Too Slow'),
        ('slow', 'Slow'),
        ('fast', 'Fast')
    ], string='Communication')
    company_image = fields.Selection([
        ('small', 'Small'),
        ('moderate', 'Moderate'),
        ('big', 'Big')
    ], string='Company Image')

    