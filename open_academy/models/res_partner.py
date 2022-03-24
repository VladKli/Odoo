# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    is_instructor = fields.Boolean(string='Instructor')
    session_ids = fields.Many2many('session', string='Course sessions')
