from odoo import _, api, fields, models
import collections
from odoo.exceptions import ValidationError


class ProductProduct(models.Model):
    _inherit = 'product.product'
    _sql_constraints = [('internal_reference_must_uniq', 'unique(default_code)', 'Internal Reference Must Be Unique!')]

    # @api.constrains('default_code')
    # def _constrains_default_code(self):
    #     for this in self:
    #         data = self.env['product.product'].search([]).mapped('default_code')
    #         dup = len([item for item, count in collections.Counter(data).items() if count > 1 and item])
    #         if dup > 0:
    #             raise ValidationError("Internal Reference Already Exist!")


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    _sql_constraints = [('internal_reference_must_uniq', 'unique(default_code)', 'Internal Reference Must Be Unique!')]

    code_product_vendor = fields.Char(compute='_compute_code_product_vendor', string='Code Product Vendor')
    
    # @api.constrains('default_code')
    # def _constrains_default_code(self):
    #     for this in self:
    #         data = self.env['product.product'].search([]).mapped('default_code')
    #         dup = len([item for item, count in collections.Counter(data).items() if count > 1 and item])
    #         if dup > 0:
    #             raise ValidationError("Internal Reference Already Exist!")


    @api.depends('seller_ids')
    def _compute_code_product_vendor(self):
        for i in self:
            d = ''
            for l in i.seller_ids:
                if l.product_code:
                    d += l.product_code + '| '
                else:
                    d = d
            i.code_product_vendor = d