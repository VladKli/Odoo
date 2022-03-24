# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import datetime


class Course(models.Model):
    _name = 'course'
    _description = 'open_academy.open_academy'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    user_id = fields.Many2one('res.users', string='User')
    session_ids = fields.One2many('session', 'course_id')

    _sql_constraints = [
        ('check_name_and_description', 'CHECK(name <> description)', 'Course description and the course title should be different'),
        ('check_name_unique', 'UNIQUE (name)', 'Course’s name should not repeat')
    ]

    def copy(self, default={}):
        default['name'] = 'Copy of ' + self.name
        rtn = super(Course, self).copy(default=default)
        return rtn


class Session(models.Model):
    _name = 'session'
    _description = 'session model'

    name = fields.Char(string='Name')
    start_date = fields.Date(string='Start day', default=datetime.date.today())
    duration = fields.Integer(string='Duration')
    seats_num = fields.Integer(string='Number of seats')
    percent_seats = fields.Integer(string='Percentage of taken seats', compute='_compute_percent_seats')
    instructor_id = fields.Many2one('res.partner', string='Instructor', domain="['|','|',('is_instructor', '=', True), ('category_id.name', '=', 'Teacher / Level 1'), ('category_id.name', '=', 'Teacher / Level 2')]")
    course_id = fields.Many2one('course', string='Course', required=True)
    attendees_ids = fields.Many2many('res.partner', string='Attendees')
    attendees_num = fields.Integer(string='Number of attendees', compute='_compute_attendees_num', store=True)
    active = fields.Boolean(string='Active', default=True)

    @api.depends('attendees_ids')
    def _compute_attendees_num(self):
        for rec in self:
            rec.attendees_num = len(rec.attendees_ids)

    @api.depends('seats_num', 'attendees_ids')
    def _compute_percent_seats(self):
        for rec in self:
            attendees_amount = len(rec.attendees_ids)
            if not rec.seats_num:
                rec.percent_seats = 0
            else:
                rec.percent_seats = (attendees_amount/rec.seats_num) * 100

    @api.onchange('seats_num', 'attendees_ids')
    def _onchange_seats_participant(self):
        if self.seats_num < 0:
            return {
                'warning': {
                    'title': "Something bad happened",
                    'message': "Number of seats can not be negative",
                }
            }
        if self.seats_num < len(self.attendees_ids):
            return {
                'warning': {
                    'title': "Something bad happened",
                    'message': "More participants than seats",
                }
            }

    @api.constrains('instructor_id', 'attendees_ids')
    def _check_instructor(self):
        for rec in self:
            if rec.instructor_id in rec.attendees_ids:
                raise ValidationError('Instructor can not present in attendees of his/her own session')
