# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
import logging

logger = logging.getLogger(__name__)

class Teacher(models.Model):
    _name = 'academy.teacher'
    _description = 'encapsulate teachers information in academy'

    name = fields.Char(string="Teacher Name")
    biography = fields.Html()

    course_ids = fields.One2many('product.template', 'teacher_id', string="Courses")
    major_ids = fields.Many2many('academy.major', string="Majors")

class Course(models.Model):
    _inherit = 'product.template'
    _description = 'encapsulate courses information'
    ref = fields.Char(string="Course Code", readonly=True)

    teacher_id = fields.Many2one('academy.teacher', string="Teacher Name")
    major_ids = fields.Many2many('academy.major', string="Majors")

    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('product.template')
        return super(Course, self).create(vals)
    
    @api.onchange('major_ids')
    def _onchange_major_ids(self):
        teachers = self.env['academy.teacher'].search([('major_ids', 'in', self.major_ids.ids)])
        if self.major_ids.ids:
            res = {
                'domain':{
                    'teacher_id':[(
                        'id', 'in', teachers.ids,
                    )]
                }
            }
        else:
            return
        return res

    @api.onchange('teacher_id')
    def _onchange_teacher_id(self):
        teachers = self.env['academy.teacher'].search([('major_ids', 'in', self.major_ids.ids)])
        if self.teacher_id and self.teacher_id not in teachers:
            warning = {
                'title': "warning",
                'message': "this is the warning message"
            }
            return {'warning': warning}
        else:
            return

class Major(models.Model):
    _name = 'academy.major'
    _description = "encapsulate majors information"
    name = fields.Char(string="Major Name")