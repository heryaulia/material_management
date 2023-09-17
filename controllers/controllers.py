import json
from odoo import http
from odoo.http import request
from werkzeug.wrappers import Response

class MaterialController(http.Controller):

    def _send_json_response(self, code, message):
        return {"code": code, "message": message}

    def _send_json_response_delete(self, code, message):
        response = Response(
            '{"code": %d, "message": "%s"}' % (code, message),
            status=code,
            content_type='application/json'
        )
        return response

    def _check_missing_params(self, params, required_params):
        return [p for p in required_params if p not in params]

    @http.route('/api/materials', type='http', auth='public', methods=['GET'])
    def get_all_materials(self, **kwargs):
        materials = request.env['material.management'].search_read([], fields=['code', 'name', 'type', 'buy_price', 'supplier_id'])
        return json.dumps(materials)

    @http.route('/api/materials', type='json', auth='public', methods=['POST'], csrf=False)
    def create_material(self, **kwargs):
        try:
            params = request.jsonrequest.get('params', {})
            required_params = ["code", "name", "type", "buy_price", "supplier_id"]
            
            missing_params = self._check_missing_params(params, required_params)
            if missing_params:
                return self._send_json_response(400, f"Missing required parameters: {', '.join(missing_params)}")
            
            supplier_id = params.get("supplier_id")
            supplier_exists = request.env['supplier.management'].search_count([('id', '=', supplier_id)])

            if not supplier_exists:
                return self._send_json_response(400, "Supplier_id not exists.")

            material = request.env['material.management'].create(params)
            return self._send_json_response(200, f"Material created successfully with ID: {material.id}!")

        except Exception as e:
            return self._send_json_response(500, str(e))

    @http.route('/api/materials/<int:material_id>', type='json', auth='public', methods=['PUT'], csrf=False)
    def update_material(self, material_id, **kwargs):
        try:
            material = request.env['material.management'].browse(material_id)

            if not material.exists():
                return self._send_json_response(404, "Material with provided ID does not exist.")
            
            material.write(kwargs)
            return self._send_json_response(200, "Material updated successfully!")
        
        except Exception as e:
            return self._send_json_response(500, str(e))

    @http.route('/api/materials/<int:material_id>', type='http', auth='public', methods=['DELETE'], csrf=False)
    def delete_material(self, material_id):
        try:
            material = request.env['material.management'].browse(material_id)

            if not material.exists():
                return self._send_json_response_delete(404, "Material with provided ID does not exist.")

            material.unlink()

            return self._send_json_response_delete(200, "Material deleted successfully!")

        except Exception as e:
            return self._send_json_response_delete(500, str(e))


