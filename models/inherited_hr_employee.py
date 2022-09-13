from odoo import api, fields, models, _


class employee_loan(models.Model):
    _inherit = "hr.employee"

    allowed_loan_limit = fields.Integer(defualt=1000)
    total_loan_amount = fields.Integer("Total Loan Amount", defualt=0, compute="_compute_total_loan_amount")
    loans = fields.One2many('employee.loan', 'employee_id', domain=[('state', '=', 'confirmed')])

    def _compute_total_loan_amount(self):
        for record in self:
            total = self.env['employee.loan'].search([('state', '=', 'confirmed'), ('employee_id', '=', record.id)])
            self.total_loan_amount = sum(total.mapped('amount'))
