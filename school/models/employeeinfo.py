from odoo import models, fields, api,_
class EmployeeInfo(models.Model):
    _name='school.employeeinfo'
    _description='Employee Info'

    
    name = fields.Char(string="Name",required=True)
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female'),
        ('others','Others')
    ], string='Gender',required=True, default='male')
    email = fields.Char(string="Email",required=True)
    phone = fields.Integer(string="Phone No")
    address = fields.Text(string="Address")

