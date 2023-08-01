from odoo import models, fields, api, _
from datetime import datetime

class CreateMeetWiz(models.TransientModel):
    _name = "school.meeting.wizard"
    _description = "School Meeting Wizard"
     

    date_meet = fields.Date(string='Date')
    name_id = fields.Many2one("school.student",required=True)
    teacher_id = fields.Many2one("school.teacher",required=True)
    note = fields.Char(String="Purpose ",required=True)

    def action_create_meeting(self):
        vals = {
            'name_stud_id' : self.name_id.id,
            'teacher_stud_id' : self.teacher_id.id,
            'notee' : self.note
        }
        meet_rec = self.env['school.meet'].create(vals)
        print('meeting', meet_rec.id)
        return {
            'name': _('Meeting'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'school.meet',
            'res_id' : meet_rec.id,
            'target' : 'new',
        }

    