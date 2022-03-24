# -*- coding: utf-8 -*-

from odoo import models, fields, api


class WizardCourse(models.TransientModel):
    _name = 'course.wizard'
    _description = 'wizard for the course'

    def get_session(self):
        return self.env['session'].browse(self.env.context.get('active_ids'))

    session_ids = fields.Many2many('session', string='Sessions', default=get_session)
    attendees_ids = fields.Many2many('res.partner', string='Attendees')

    def add_attendees_to_session(self):
        for session in self.session_ids:
            session.attendees_ids += self.attendees_ids
        return {}
