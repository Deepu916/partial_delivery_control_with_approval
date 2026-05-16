# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ApprovalRequest(models.Model):
    _name = 'approval.request'
    _description = 'Approval Request'


    delivery_id = fields.Many2one('stock.picking')
