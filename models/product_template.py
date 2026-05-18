# -*- coding: utf-8 -*-
"""Product template model"""
from odoo import fields, models


class ProductTemplate(models.Model):
    """Product template model"""
    _inherit = "product.template"

    allow_partial_delivery = fields.Boolean(string="Allow partial delivery")
