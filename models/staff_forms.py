from odoo import models, fields, api, _


class LogicStaffForms(models.Model):
    _name = 'logic.staff_forms'
    _description = 'Staff Forms'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name')
    address = fields.Char(string='Address')
    date_of_joining = fields.Date(string='Date of Joining')
    dob = fields.Date(string='Date of Birth')
    personal_mail_id = fields.Char(string='Personal Mail ID')
    office_mail_id = fields.Char(string='Office Mail ID')
    phone_number = fields.Char(string='Phone Number')
    office_number = fields.Char(string='Office Number')
    branch_id = fields.Many2one('logic.base.branches', string='Branch')

    aadhar_card = fields.Binary(string='Aadhar Card')
    bank_passbook = fields.Binary(string='Bank Passbook')
    sslc_certificate = fields.Binary(string='SSLC Certificate')
    passport_size_photo = fields.Binary(string='Passport Size Photo')
