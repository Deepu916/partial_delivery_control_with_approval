# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    allow_partial_delivery = fields.Boolean(string="Allow partial delivery")