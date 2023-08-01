from odoo import models, fields, api,_
class meet(models.Model):
    _name='school.meet'
    _description='Meeting'

    date_meet = fields.Date(string='Date')
    name_stud_id = fields.Many2one('school.student',string='Student Name',required=True)
    teacher_stud_id = fields.Many2one('school.teacher',string='Teacher Name',required=True)
    notee = fields.Char(string='Description',required=True)

    # meet_count = fields.Integer(string='Meeting Count') 
    # (,compute='compute_meet_count')

    # meeting_count = fields.Integer(string='Meeting Count',compute='compute_meeting_count')


# @api.depends('name_stud_id')
# def compute_meeting_count(self):
#     for rec in self:
#         meet_count = self.env['school.meet'].search_count([('name_stud_id', '=' ,rec.name_stud_id.id )])
#         rec.meeting_count = meet_count

    meeting_count = fields.Integer(string='Meeting Count',compute = 'compute_meeting_count')
    

    def compute_meeting_count(self):
        for rec in self:

            meeting_count = self.env['school.meet'].search_count([('name_stud_id', '=',rec.id )])
            rec.meeting_count = meeting_count
