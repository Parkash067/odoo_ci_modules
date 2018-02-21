{

    'name'  :   'Custom Reports',
    'summery'   :  'Custom Module for the all Invoices Format',
    'description': """""",
    'author': "",
    'category': '["Account"]',
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'version': '0.1',
    # any module necessary for this one to work correctly

    'depends':   [
        'base',
        'account',
    ],
    'data': [
        'views/custom_sale_invoice.xml','custom_reports.xml',
    ]

}