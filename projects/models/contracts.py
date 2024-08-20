from odoo import models, fields

class Projects(models.Model):
    _name = 'projects'
    _description = 'Projects'

    company_name = fields.Char('اسم الشركة')
    customer_name = fields.Char('اسم العميل')
    plote_number = fields.Char('رقم القسيمة')
    contract_type = fields.Selection([
        ('type1', 'نوع 1'),
        ('type2', 'نوع 2'),
    ], string='نوع العقد')
