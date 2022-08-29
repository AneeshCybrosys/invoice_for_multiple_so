# -*- coding: utf-8 -*-
from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = "account.move"

    sale_order_ids = fields.Many2many('sale.order', string='Related Sale '
                                                           'Orders',
                                      domain="[('state', '=', 'sale')]")

    @api.onchange("sale_order_ids")
    def _onchange_sale_order(self):
        self.line_ids = False
        order_lines = self.env['sale.order.line'].search(
            [('order_id', 'in', self.sale_order_ids.ids)])
        for orders in order_lines:
            self.line_ids = [(0, 0, {'product_id': orders.product_id,
                                     'name': orders.name,
                                     'quantity':
                                         orders.product_uom_qty,
                                     'price_unit':
                                         orders.price_unit,
                                     'currency_id':
                                         self.env.user.company_id.currency_id.id,
                                     'price_subtotal': orders.price_subtotal,
                                     'account_id': self.env[
                                         'account.account'].search(
                                         [('name', '=', 'Local '
                                                        'Sales')]).id,
                                     })]
        print(self.line_ids, "gdfg")
        self._move_autocomplete_invoice_lines_values()
