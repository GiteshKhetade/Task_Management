from odoo import models, fields, api,_
class CompanyInfo(models.Model):
    _name='school.companyinfo'
    _description='Company Info'

    
    name = fields.Char(string="Company Name",required=True)
    cemail = fields.Char(string="Company Email",required=True)
    cphone = fields.Integer(string="Company Phone_No")
    caddress = fields.Text(string="Company Address")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")


    