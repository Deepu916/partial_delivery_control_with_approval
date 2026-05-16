# -*- coding: utf-8 -*-
from odoo import api, fields, models


class PartialDeliveryApprove(models.TransientModel):
    _name = 'wizard.partial.delivery.approve'


    delivery_id = fields.Many2one('stock.picking')

    def action_approval_send(self):
        self.env['approval.request'].create({
            'delivery_id': self.delivery_id.id,
        })
