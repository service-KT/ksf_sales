from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection(selection_add=[('waiting', 'Waiting Payment'),('sale',)])

    def action_confirm(self):
        for order in self:
            if order.payment_term_id.id != 1:
                # If immediate payment is not required, proceed with the normal confirmation process
                super(SaleOrder, order).action_confirm()
            else:
                # Otherwise, set the state to 'waiting'
                order.write({'state': 'waiting'})
        return True

    def action_payment_receive(self):
        for order in self:
            super(SaleOrder, order).action_confirm()
        return True
