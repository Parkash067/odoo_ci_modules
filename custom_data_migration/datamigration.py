#The file name of this file must match the filename name which we import in __init__.py file
# -*- coding: utf-8 -*-
from openerp.osv import fields, osv
from openerp import api
from datetime import datetime,date,time,timedelta
import qrcode
import base64
import cStringIO


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
        'partner_id': fields.char('Customer', store=True),
        'invoice_number': fields.char('Invoice Number', store=True),
        'do_number': fields.char('DO Number', store=True),
        'state': fields.selection([('draft', 'Draft'), ('confirmed', 'Confirmed')], 'State', store=True, default='draft'),
        'date': fields.date('Date', store=True, required=True),
        'products': fields.one2many('custom.invoice.lines', 'invoice', 'Products',store=True, states={'confirmed': [('readonly', True)]}),
        'amount_total': fields.float('Total', store=True)
    }


class custom_invoice_lines(osv.osv):
    _name = "custom.invoice.lines"
    _rec_name = 'product_id'
    _columns = {
        'product_id': fields.many2one('custom.products', 'Engine Number',store=True),
        'chasis_number': fields.related('product_id', 'chasis_number', type='char', string='Chasis Number', readonly=True),
        'c_c': fields.related('product_id', 'c_c', type='char',string='CC', readonly=True),
        'price': fields.float('Unit Price', store=True),
        'quantity': fields.float('Quantity', store=True),
        'invoice': fields.many2one('custom.invoice', 'Invoice', store=True),
        'do_number': fields.related('invoice', 'do_number', type='char', string='DO Number',readonly=True),
        'certificate_issuance': fields.integer('Issunance Times', store=True, default=0),
        'qr_code': fields.binary('QR Code', store=True)
    }

    def generate_qr_code(self):
       return "Engine Number : "+str(self.product_id.engine_number) + "\n" + "Chasis Number : " + str(self.product_id.chasis_number) + "\n" + "Model : " + self.product_id.model + "\n"+ "Brand : " + self.product_id.brand + "\n" +"HP : " + self.product_id.c_c + "\n" +" 'MANUFACTURED BY SARA AUTOMOBILE INDUSTERIES'"

    def issuance(self):
        self.certificate_issuance = 1
        return ''

    def check_issuance(self):
        return int(self.certificate_issuance)



class products(osv.osv):
    _name = "custom.products"
    _rec_name = "engine_number"
    _columns = {
        "engine_number": fields.char('Engine Number', store=True),
        "chasis_number": fields.char('Chasis Number', store=True),
        "color": fields.char('Color', store=True),
        "model": fields.char('Model', store=True),
        "brand": fields.char('Brand', store=True),
        "c_c": fields.char('CC', store=True),
        "date": fields.date('Date', store=True)
    }


class ledgers(osv.osv):
    _name = "custom.ledgers"
    _rec_name = "account_id"
    _columns = {
        'date': fields.date('Date', store=True),
        'customer': fields.char('Customer', store=True),
        'account_id': fields.char('Account', store=True),
        'ref': fields.char('Ref', store=True),
        'narration': fields.char('Narration', store=True),
        'debit': fields.float('Debit', store=True),
        'credit': fields.float('Credit', store=True),
        'balance': fields.float('Balance', store=True),
    }