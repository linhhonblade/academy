# -*- coding: utf-8 -*-

from odoo import models, fields


class Teacher(models.Model):
    _name = 'academy.teacher'
    _description = 'encapsulate teachers information in academy'

    name = fields.Char()
    biography = fields.Html()

    course_ids = fields.One2many('product.template', 'teacher_id', string="Courses")
    major_ids = fields.Many2many('academy.major', string="Majors")


class Course(models.Model):
    _inherit = 'product.template'
    _description = 'encapsulate courses information'

    name = fields.Char()
    teacher_id = fields.Many2one('academy.teacher', string="Teacher")
    major_ids = fields.Many2many('academy.major', string="Majors")


class Major(models.Model):
    _name = 'academy.major'
    _description = "encapsulate majors information"
    
    name = fields.Char()
