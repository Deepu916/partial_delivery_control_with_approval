# -*- coding: utf-8 -*-
"""System Configuration model"""
import ast
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    """System Configuration model"""
    _inherit = 'res.config.settings'


    partial_delivery_approval_user_ids = fields.Many2many('res.users',
                                                         string='Partial delivery approval users',
                                                         )
    def set_values(self):
        """Set values for this setting"""
        super(ResConfigSettings,self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('stock_picking.partial_delivery_approval_user_ids', self.partial_delivery_approval_user_ids.ids)

    def get_values(self):
        """Get values for this setting"""
        res = super(ResConfigSettings,self).get_values()
        value = self.env['ir.config_parameter'].sudo().get_param('stock_picking.partial_delivery_approval_user_ids')
        user_ids = ast.literal_eval(value) if value else []
        res.update(partial_delivery_approval_user_ids = [fields.Command.set(user_ids)])
        return res
