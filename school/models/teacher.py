from odoo import models, fields, api,_

class teacher(models.Model):
    _name='school.teacher'
    
    _inherit =['mail.thread','mail.activity.mixin']
    
    _description='Teachers'

    _order ='id desc'

    # sequence = fields.Integer(string='Sequence', default=_('New'), help='The sequence number for this teacher',)

    # school_teachers = fields.One2many('ir.sequence', 'school.teacher_id', string='School Teachers',)

    name = fields.Char(string='Name',tracking= True,required = True)
    gender = fields.Selection([
        ('select', 'Select Gender'),
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    ], string='Gender', required=True, tracking= True, default='select')
    address = fields.Char(string='Address')
    city = fields.Char(string='City')
    mobile_no = fields.Char(string='Mobile No')
    email_address = fields.Char(string='Email Address')
    qualification = fields.Char(string='Qualification')
    designation = fields.Char(string='Designation')
    specailization = fields.Char(string='Specailization')
    experience = fields.Char(string='Experience')
    sequence = fields.Char(string='Sequence', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    image = fields.Binary(string="Teacher Image")
    # course_ids = fields.One2many(string='Teaching Course',comodel_name='school.course',inverse_name='clteacher_id',readonly=True) 
    course_id = fields.Many2one(string='Course Details', comodel_name='school.course', ondelete='restrict')
    @api.model
    def create(self, vals):
        print("In create vals: ",vals)
        if vals.get('sequence', _('New')) == _('New'):
            vals['sequence'] = self.env['ir.sequence'].next_by_code('school.teacher') or _('New')
        return super(teacher,self).create(vals)




class teacherlines(models.Model):
     _name='school.teacherlines' 
     _description='Teachers Lines'

     name=fields.Char(string='Name')
     designation = fields.Char(string='Designation')
     specailization = fields.Char(string='Specailization')
     experience = fields.Char(string='Experience')
     tea_id = fields.Many2one(string='Teacher name', comodel_name='school.teacher', ondelete='restrict')