from odoo import http
from odoo.http import request
import io
import base64


class WebsiteForm(http.Controller):
    @http.route(['/staff_form'], type='http', auth="public", website=True)
    def appointment(self):
        partners = request.env['employee.module.form'].sudo().search([])
        branch = request.env['logic.base.branches'].sudo().search([])
        values = {}
        values.update({
            'partners': partners,
            'branch': branch
        })
        return request.render("data_collection.staff_form_web_view", values)

    @http.route(['/staff_form/submit'], type='http', csrf=False, auth='public', website=True, method=['POST'])
    def datas_upload(self, **kw):

        photo = kw.get('upload_phone')
        aadhar = kw.get('upload_aadhar')
        sslc = kw.get('upload_sslc')
        baank = kw.get('upload_passbook')

        request.env['logic.staff_forms'].sudo().create({
            'name': kw.get('employee_name'),
            'personal_mail_id': kw.get('mail_id'),
            'office_number': kw.get('office_number'),
            'phone_number': kw.get('phone_number'),
            'office_mail_id': kw.get('office_mail_id'),
            'address': kw.get('address'),
            'dob': kw.get('birth'),
            'date_of_joining': kw.get('joining'),
            'branch_id': kw.get('branch'),
            'passport_size_photo': base64.b64encode(photo.read()),
            'aadhar_card': base64.b64encode(aadhar.read()),
            'sslc_certificate': base64.b64encode(sslc.read()),
            'bank_passbook': base64.b64encode(baank.read()),
        })
        print('ok', kw)
        return request.render("data_collection.logic_staff_form_success")
