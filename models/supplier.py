from odoo import api, fields, models

class Supplier(models.Model):
    _name = 'supplier.management'
    _description = 'Supplier Management'

    name = fields.Char('Supplier Name', required=True)
    contact = fields.Char('Supplier Contact Number')
    address = fields.Char('Supplier Address')
    email = fields.Char('Supplier Email')
