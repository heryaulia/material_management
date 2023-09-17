# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Material(models.Model):
    _name = 'material.management'
    _description = 'Material Management'

    code = fields.Char('Material Code', required=True)
    name = fields.Char('Material Name', required=True)
    type = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton')
    ], 'Material Type', required=True)
    buy_price = fields.Float('Material Buy Price', required=True)
    supplier_id = fields.Many2one('supplier.management', 'Related Supplier', required=True)

    @api.constrains('code')
    def _check_unique_code(self):
        for record in self:
            if self.env['material.management'].search_count([('code', '=', record.code)]) > 1:
                raise ValidationError('Material Code must be unique!')

    @api.constrains('buy_price')
    def _check_buy_price(self):
        for record in self:
            if record.buy_price < 100:
                raise ValidationError('Material Buy Price must be >= 100.')


