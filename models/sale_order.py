from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    ​state = fields.Selection(selection_add=[('waiting', 'Waiting Payment')])

    ​def action_quote_confirm(self):
    for order in self:
        is_immediate_payment = order.your_method_to_check_payment()  # Access `order` to check individually
        if not is_immediate_payment:
            super(SaleOrder, order).action_confirm()  # Confirm this specific order
        else:
            order.write({'state': 'waiting'})  # Set to waiting if immediate payment is needed

    return True
