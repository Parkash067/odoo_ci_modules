#The file name of this file must match the filename name which we import in __init__.py file
# -*- coding: utf-8 -*-
from openerp.osv import fields, osv
from openerp import api
from datetime import datetime,date,time,timedelta


class fp_customers(osv.osv):
    _name = 'fp.customers'
    _rec_name = 'name'
    _columns = {
        'name': fields.char('Name', store=True),
        'fp_id': fields.char('Foxpro ID', store=True)
    }


class custom_invoice(osv.osv):
    _name = "custom.invoice"
    _rec_name = 'invoice_number'
    _columns = {
        'partner_id': fields.many2one('fp.customers', string='Customer', store=True),
        'invoice_number': fields.char('Invoice Number', store=True),
        'do_number': fields.char('Invoice Number', store=True),
        'state': fields.selection([('draft', 'Draft'), ('confirmed', 'Confirmed')], 'State', store=True, default='draft'),
        'date': fields.date('Date', store=True, required=True),
        'products': fields.one2many('custom.invoice.lines', 'invoice', 'Products',store=True, states={'confirmed': [('readonly', True)]}),
        'amount_total': fields.float('Total', store=True)
    }


class custom_invoice_lines(osv.osv):
    _name = "custom.invoice.lines"
    _rec_name = 'product'
    _columns = {
        'product': fields.char('Product', store=True),
        'name': fields.char('Description', store=True),
        'price': fields.float('Unit Price', store=True),
        'quantity': fields.float('Quantity', store=True),
        'invoice': fields.many2one('custom.invoice', 'Invoice', store=True),
    }
