# -*- coding: utf-8 -*-
from odoo import fields, models
from odoo.exceptions import ValidationError


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def button_validate(self):
        if self.picking_type_code == 'outgoing':
            for ids in self.move_ids:
                if not ids.product_id.allow_partial_delivery:
                    if ids.product_uom_qty > ids.quantity:
                        return {
                            'name':'Partial delivery approval request',
                            'type':'ir.actions.act_window',
                            'res_model': 'wizard.partial.delivery.approve',
                            'view_mode': 'form',
                            'target': 'new',
                            'context': {'default_delivery_id':self.id}
                        }
                    super().button_validate()
        super().button_validate()

    def action_approval_request(self):
        return{
            'name': 'Partial delivery approval request',
            'type': 'ir.actions.act_window',
            'res_model': 'approval.request',
            'view_mode': 'list',
            'domain': [('delivery_id','=',self.id)]
        }