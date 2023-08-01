from odoo import models, fields, api,_
class course(models.Model):
    _name='school.course'
    _description='Meeting'
    _rec_name="name"


    name = fields.Char(string='Course Name',required=True)
    sem = fields.Char(string='Semester Name',required=True)
    department = fields.Char(string='Deaprtment Name')
    teach_ids = fields.One2many(string='Teacher Assign',comodel_name='school.teacherlines',inverse_name='tea_id' )
    # clteacher_id = fields.Many2one('school.teacher',string='Class Teacher',required=True)

    