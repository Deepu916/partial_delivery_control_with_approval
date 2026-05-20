# -*- coding: utf-8 -*-
"""Stock picking model"""
import ast
from odoo import fields, models


class StockPicking(models.Model):
    """Stock picking model"""
    _inherit = 'stock.picking'


    state = fields.Selection(selection_add=[('approval','Approval Waiting'),('assigned','Ready')])
    user_ids = fields.Many2many('res.users', string='Users',compute='_compute_user_ids')
    partial_delivery_line = fields.Boolean(string='Partial delivery line')


    def _compute_user_ids(self):
        """Compute approval user ids"""
        for record in self:
            value = self.env['ir.config_parameter'].sudo().get_param(
                'stock_picking.partial_delivery_approval_user_ids')
            users_ids = ast.literal_eval(value) if value else []
            record.user_ids = [fields.Command.set(users_ids)]


    def button_validate(self):
        """Validate the stock picking operation"""
        print("validate", self.state, self.env.context.get('skip_partial_approval'))

        if self.env.context.get('skip_partial_approval'):
            print("Approved")
            self.state ='assigned'
            return super().button_validate()

        if self.picking_type_code == 'outgoing':
            for ids in self.move_ids:
                if not ids.product_id.allow_partial_delivery:
                    if ids.product_uom_qty > ids.quantity:
                        self.partial_delivery_line = True
                        break
            if self.partial_delivery_line and self.env.user.id not in self.user_ids.ids:
                self.write({'state': 'approval'})
                return True
            print("validate")
            return super().button_validate()
        return super().button_validate()


    def action_approved(self):
        """Approve stock picking"""
        return  self.with_context(skip_partial_approval = True).button_validate()
