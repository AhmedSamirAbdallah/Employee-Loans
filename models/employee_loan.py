from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from datetime import date, datetime, time


class employee_loan(models.Model):
    _name = "employee.loan"
    _rec_name = "employee_id"

    employee_id = fields.Many2one('hr.employee')
    amount = fields.Integer(defualt=0)
    start_date = fields.Date("Start Date")
    end_date = fields.Date("End Date")
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('ended', 'End'),
    ], string='state', required=True, readonly=True,
        default='draft')
    user_id = fields.Many2one('res.users', default=lambda self: self.env.user.id)

    def button_draft(self):
        for record in self:
            record.state = "draft"

    def button_confirmed(self):
        for record in self:
            record.state = "confirmed"

    def button_cancelled(self):
        for record in self:
            record.state = "cancelled"

    def button_ended(self):
        for record in self:
            record.state = "ended"

    def write(self, vals):
        if 'state' in vals.keys():
            self.user_id = self.env.user.id
        return super(employee_loan, self).write(vals)

    @api.constrains('amount', 'state')
    def _check_valid_loan(self):
        for record in self:
            if record.employee_id.total_loan_amount > record.employee_id.allowed_loan_limit:
                raise ValidationError(
                    'you reach to the limit of the total loans'
                )

    def change_state_after_end_date(self):
        for record in self.search([]):
            if record.end_date == date.today():
                record.state = "ended"
