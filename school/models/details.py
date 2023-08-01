from odoo import models, fields, api,_ 

class details(models.Model):

    _name='school.details'

    _description='Details'

    name_id = fields.Many2one('school.student',required = True)
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female'),
        ('others','Others')
    ], string='Gender',required=True, default='male')
    address = fields.Char(string='Address',related='name_id.address')
    city = fields.Char(string='City',related='name_id.city')
    state = fields.Char(string='State')
    mobile_no = fields.Char(string='Mobile No',related='name_id.mobile_no')
    email_address = fields.Char(string='Email Address',related='name_id.city')
    medicine_info_ids = fields.One2many("school.medical.info","medical_id",string ="Student Medicine Information")

    medical = fields.Text(string="Medical History")
    
    
    # medical_det = fields.Text(string="Medical Information")
    # teacher_name_id = fields.Many2one('school.teacher')
    # qualification = fields.Char(string='Qualification')
    # specailization = fields.Char(string='Specailization')

class MedicalInfo(models.Model):

    _name='school.medical.info'

    _description='Medical Information'

    name = fields.Char(string = "Medicne Info")
    quantity = fields.Integer(string = "Quantity")
    medical_id = fields.Many2one("school.details",string = "Medical Information")