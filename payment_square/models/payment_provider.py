# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
from odoo import fields, models, _


_logger = logging.getLogger(__name__)


class PaymentProvider(models.Model):
    _inherit = 'payment.provider'

    code = fields.Selection(selection_add=[('square', "Square")], ondelete={'square': 'set default'})
