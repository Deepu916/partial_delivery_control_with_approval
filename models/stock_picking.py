# -*- coding: utf-8 -*-
"""Stock picking model"""
import ast
from odoo import fields, models


class StockPicking(models.Model):
    """Stock picking model"""
    _inherit = 'stock.picking'


    is_approval_sent = fields.Boolean(string='Status')
    state = fields.Selection(selection_add=[('approval','Approval Waiting'),('done','Done')])
    user_ids = fields.Many2many('res.users', string='Users',compute='_compute_user_ids')
    partial_delivery_line = fields.Boolean(string='Partial delivery line')


    def _compute_user_ids(self):
        """Compute approval user ids"""
        for record in self:
            value = self.env['ir.config_parameter'].sudo().get_param('stock_picking.partial_delivery_approval_user_ids')
            users_ids = ast.literal_eval(value) if value else []
            record.user_ids = [fields.Command.set(users_ids)]


    def button_validate(self):
        """Validate the stock picking operation"""
        if self.picking_type_code == 'outgoing':
            res = super().button_validate()
            for ids in self.move_ids:
                if not ids.product_id.allow_partial_delivery:
                    if ids.product_uom_qty > ids.quantity:
                        self.partial_delivery_line = True
                        break
            if self.partial_delivery_line:
                self.write({'state': 'approval', 'is_approval_sent': True})
            return res
        # super().button_validate()

    def action_approved(self):
        """Approve stock picking"""
        self.button_validate()
        self.is_approval_sent = False
