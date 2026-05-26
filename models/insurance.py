# -*- coding: utf-8 -*-

from odoo import models, fields, api, _ 
from odoo.exceptions import ValidationError 

class InsuranceDownReason(models.Model):
    _name = 'insurance.down.reason'
    _description = 'Insurance Down Reason Management'
    _order = 'description'

    _sql_constraints = [
        ('unique_description', 'unique(description)', 'There cannot be two Insurance Down Reasons with the same description.')
    ]

    description = fields.Text('Description')



class InsurancePolicy(models.Model):
    _name = 'insurance.policy'
    _description = 'Insurance Policy'
    _order = 'id desc'

    id = fields.Integer('Policy Number', required=True)

    name = fields.Char('Name', required=True)

    cover_date = fields.Date('Cover Date', required=True) # Data fins a la que es cobreix l'assegurança
    cover_hour = fields.Integer('Cover Hour', required=True) # Hora de final de cobertura
    cancel_date = fields.Date('Cancel Date') # Opcional

    effective_date = fields.Date('Effective Date', compute='_compute_effective_date')
    
    maturity_type = fields.Selection([('anual', 'Anual'), ('semi-anual', 'Semi-anual'), ('quarterly', 'Quarterly'), ('monthly', 'Monthly')], 'Maturity Type', required=True)
    insured_object = fields.Text('Insured Object', required=True)


    # Producte (product.product)
    product_id = fields.Many2one('product.product', 'Product', required=True)
    product_name = fields.Char(related='product_id.name', string='Product Name', store=True)

    # Client (res.partner)
    client_id = fields.Many2one('res.partner', 'Client', required=True)
    client_name = fields.Char(related='client_id.name', string='Client Name', store=True)

    # Proveïdor (res.partner)
    provider_id = fields.Many2one('res.partner', 'Provider', required=True)

    # Motiu de baixa (insurance.down)
    down_reason_id = fields.Many2one('insurance.down.reason', 'Insurance Down Reason') # Opcional mentres l'assegurança sigui vigent

    @api.depends('id', 'client_name', 'product_name')
    def _compute_display_name(self):
        for record in self:
            if record.client_name != False and record.product_name != False:
                record.display_name = record.id + " - " + record.client_name + " - " + record.product_name
            else:
                record.display_name = "New Insurance Policy"

    def _compute_effective_date(self):
        for policy in self:
            policy.effective_date = fields.Date.today()

    # La data efectiva no pot ser anterior a la data actual
    @api.constrains('effective_date')
    def _check_effective_date(self):
        for policy in self:
            if policy.effective_date < fields.Date.today():
                raise ValidationError(_('The Effective Date cannot be before the current date.'))