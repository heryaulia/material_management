from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestMaterial(TransactionCase):

    def setUp(self):
        super(TestMaterial, self).setUp()
        self.Material = self.env['material.management']
        self.Supplier = self.env['supplier.management']

    def test_create_material(self):
        supplier = self.Supplier.create({'supplier_name': 'Test Supplier'})
        material = self.Material.create({
            'material_code': 'M001',
            'material_name': 'Test Material',
            'material_type': 'fabric',
            'material_buy_price': 120,
            'related_supplier_id': supplier.id
        })
        self.assertEqual(material.material_code, 'M001')
    
    def test_invalid_price(self):
        supplier = self.Supplier.create({'supplier_name': 'Test Supplier'})
        with self.assertRaises(ValidationError):
            self.Material.create({
                'material_code': 'M002',
                'material_name': 'Invalid Material',
                'material_type': 'fabric',
                'material_buy_price': 80,
                'related_supplier_id': supplier.id
            })
