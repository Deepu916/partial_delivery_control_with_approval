{
    'name': 'Partial Delivery Control',
    'version': '19.0.1.0.0',
    'description': """Partial Delivery Control by Approvals""",
    'depends': ['stock', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/stock_picking_views.xml',
        'views/approval_request_views.xml',
        'wizard/partial_delivery_approve_views.xml',
        'views/res_config_settings_views.xml',
        'views/product_template_views.xml',

    ]
}
