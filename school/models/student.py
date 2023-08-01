from odoo import models, fields, api,_
from odoo.exceptions import ValidationError
class student(models.Model):
    _name='school.student'
    _description='Student'
    
    
    name = fields.Char(string='Name',required=True)
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female'),
        ('others','Others')
    ], string='Gender',required=True, default='male')
    address = fields.Char(string='Address')
    city = fields.Char(string='City')
    status = fields.Char(string='status')
    mobile_no = fields.Char(string='Mobile No')
    email_address = fields.Char(string='Email Address')
    class_teacher_id = fields.Many2one('school.teacher')
    sequence = fields.Char(string='Sequence', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    standard = fields.Char(string='Standard')
    grade = fields.Char(string='Grade')
    activities = fields.Char(string='Co-curricular activities')
    achivements = fields.Char(string='Achivements')
    status = fields.Selection([('draft','Draft'),('conform','Conformed'),('done','Done'),('cancel','Canceled')],string='Status')
    stud_med_info_ids = fields.One2many("school.details","name_id",string ="Medicine Information")
    course_id = fields.Many2one("school.course",string="Enrolled Course")



    # meeting_count = fields.Integer(string='Meeting Count',compute = 'compute_meeting_count')
    

    # def compute_meeting_count(self):
    #     for rec in self:

    #         meeting_count = self.env['school.meet'].search_count([('name_stud_id', '=',rec.id )])
    #         rec.meeting_count = meeting_count


    def action_conform(self):
        self.status='conform'
        return{
            'effect':{
                'fadeout': 'fast',
                'type' : 'rainbow_man',
                'message': 'Conformed Student'
            }
        }


    def action_done(self):
        self.status='done'
    def action_cancel(self):
        self.status='cancel'
    def action_draft(self):
        self.status='draft'


    def unlink(self):
        print("delete")
        if self.status =='done':
            raise ValidationError (_("you cannot Delete %s as it is in Done State" %self.name))
        return super(student,self).unlink() 

    @api.constrains('city')
    def check_city(self):
        for rec in self:
            if rec.city == 0:
                raise ValidationError(_("City Cant be zero....!!!"))

    # def name_get(self):
    #     result = []
    #     for rec in self:
    #         name= rec.sequence + " " + rec.class_teacher_id
    #         result.append((rec.sequence,rec.class_teacher_id))
    #     return result

    @api.model
    def create(self,vals):
        if not vals.get('city'):
            vals['city'] = 'PUNE'
            res=super(student,self).create(vals)
            return res
            
    # @api.model
    # def default_get(self,fields):
    #     res = super(student,self).default_get(fields)
    #     print("overloaded")



 